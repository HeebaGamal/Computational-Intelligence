import numpy as np
from math import exp
from random import seed
from random import random
from math import exp
from random import seed
from random import random
from tkinter import *
from tkinter.messagebox import *
from tkinter import ttk
import tkinter as tk
from functools import partial
from GUI import *


# Initialize a network
def initialize_weights(neurons_input, neurons_hidden, neurons_in_each_layer, neurons_output):
    network = list()
    # assuming the 2 hidden layers are neurons input +1
    for i in range(0, neurons_hidden):  # for each layer
        hidden_layer = list()
        for j in range(0, neurons_in_each_layer[i]):  # for each neuron in the layer
            if i != 0:  # if the previous layer is not the input
                # number of weights for each neuron = number of previous neurons + bias
                hidden_layer.append({'weights': [random() for i in range(0, neurons_in_each_layer[i-1]+1)]})
            else:  # if the previous layer is the input
                # number of weights for each neuron = number of inputs + bias
                hidden_layer.append({'weights': [random() for i in range(0, neurons_input + 1)]})
        network.append(hidden_layer)  # append the layer to the network

    # output layer is the 3 classes
    # each class has a dict with weight key
    output_layer = [{'weights': [random() for i in range(neurons_in_each_layer[-1] + 1)]} for i in range(neurons_output)]
    network.append(output_layer)
    return network


def activate(weights, inputs, bias):
    activation = weights[-1]*bias
    for i in range(len(weights) - 1):
        activation += weights[i] * inputs[i]
    return activation


def sigmoid(activation):
    return 1.0 / (1.0 + exp(-activation))


def hyperbolic(activation):
    num = 1-exp(-activation)
    den = 1+exp(-activation)
    return num/den


def forward_propagate(network, row, activation_choice, bias):
    inputs = row
    for layer in network:  # on each hidden layer and output layer
        new_inputs = []
        for neuron in layer:  # on each neuron in the layer
            activation = activate(neuron['weights'], inputs, bias)
            if activation_choice.__eq__("sigmoid"):
                neuron['output'] = sigmoid(activation)  # the result of each neuron
            else:
                neuron['output'] = hyperbolic(activation)  # the result of each neuron
            new_inputs.append(neuron['output'])
        inputs = new_inputs
    return inputs


def Derivative_Activation(output):
    return output * (1.0 - output)


def backward_propagate_error(network, expected):
    #error = (expected - output) * Derivative_Activation(output)
    for i in reversed(range(len(network))):
        layer = network[i]  # for each layer starting from output layer
        errors = list()  # error list for each layer
        if i != len(network) - 1:  # if it is not the output layer
            for j in range(len(layer)):
                error = 0.0
                for neuron in network[i + 1]:  # for each neuron in the previous layer
                    error += (neuron['weights'][j] * neuron['delta'])
                errors.append(error)  # appends the error of each neuron
        else:  # if it is the output layer
            for j in range(len(layer)):
                neuron = layer[j]  # for each neuron in the layer
                errors.append(expected[j] - neuron['output'])
        for j in range(len(layer)):  # for each neuron in the layer
            neuron = layer[j]
            neuron['delta'] = errors[j] * Derivative_Activation(neuron['output'])  # calculate the delta of each neuron


def update_weights(network, row, learining_rate):
    for i in range(len(network)):  # for each layer
        inputs = row[:-1]  # takes all columns of the row except the last one (output)
        if i != 0:  # if it is not the input layer
            # consider the output of each neuron of the previous layer as input
            inputs = [neuron['output'] for neuron in network[i - 1]]
        for neuron in network[i]:  # for each neuron in the layer
            for j in range(len(inputs)):  # for all columns of the input
                neuron['weights'][j] += learining_rate * neuron['delta'] * inputs[j]  # calculate the new weights
            neuron['weights'][-1] += learining_rate * neuron['delta']  # calculate the weights of the output layer


def train_network(network, train_data, learning_rate, n_epoch, neurons_output, activation_choice, bias):
    for epoch in range(n_epoch):
        sum_error = 0
        for row in train_data:
            forward_propagate(network, row, activation_choice, bias)  # checked
            expected = [0 for i in range(neurons_output)]  # this should set all output classes with 0
            expected[int(row[-1])] = 1  # this should set the expected output class with 1

            backward_propagate_error(network, expected)
            update_weights(network, row, learning_rate)


def read_data():
    data = open("IrisData.txt", "r")
    records = data.read().split('\n')  # split the file into records/rows
    records.__delitem__(0)
    for i in range(0, len(records)):
        records[i] = records[i].split(',')  # split each record into 5 X1,X2,X3,X4,class
    data.close()

    np_array_records = np.array(records)
    X = (np_array_records[:, 0:4])  # takes the first 4 columns of the data (input)

    train_data_np = np.zeros([90, 5])
    train_data_np[:30, :-1] = X[:30, :]
    train_data_np[30:60, :-1] = X[50:80, :]
    train_data_np[60:90, :-1] = X[100:130, :]
    train_data_np[:30, -1] = 0
    train_data_np[30:60, -1] = 1
    train_data_np[60:90, -1] = 2
    train_data = train_data_np.tolist()

    test_data_np = np.zeros([60, 5])
    test_data_np[:20, :-1] = X[30:50, :]
    test_data_np[20:40, :-1] = X[80:100, :]
    test_data_np[40:60, :-1] = X[130:, :]
    test_data_np[:20, -1] = 0
    test_data_np[20:40, -1] = 1
    test_data_np[40:60, -1] = 2
    test_data = test_data_np.tolist()
    return train_data, test_data


def test(network, test_data, activation_choice, bias):
    outputs = list()
    for row in test_data:
        probability_result = forward_propagate(network, row, activation_choice, bias)  # checked
        Max_probability = max(probability_result)
        indx = probability_result.index(Max_probability)
        outputs.append(indx)
    return outputs


'''def accuracy(predicted_result, test_data):
    correct = 0
    for i in range(0, len(predicted_result)):
        if predicted_result[i] == test_data[i][-1]:
            correct += 1
    return correct/60'''
def accuracy(predicted_result, test_data):
    confusion_matrix = [[0 for i in range(4)] for j in range(4)]
    #          predicted_0      predicted_1     predicted_2     total
    # actual_0                                                 total_actual_0
    # actual_1                                                 total_actual_1
    # actual_2                                                 total_actual_2
    # total     total_pred_0    total_pred_1    total_pred_2
    for i in range(0, len(predicted_result)):
        confusion_matrix[int(test_data[i][-1])][int(predicted_result[i])] += 1
    confusion_matrix[3].pop(3)
    for i in range(3):
        for j in range(3):
            confusion_matrix[i][3] += confusion_matrix[i][j]  # total of the row
            confusion_matrix[3][i] += confusion_matrix[j][i]  # total of the column
    return confusion_matrix, (confusion_matrix[0][0]+confusion_matrix[1][1]+confusion_matrix[2][2])/60



window = Tk()
gui_obj = GUI(window)
#print(type(gui_obj))
gui_obj.GUI_input()

window.mainloop()

seed(1)
read_data()
train_data, test_data = read_data()

neurons_input = len(train_data[0]) - 1  # 2 inputs (X1,X2)
neurons_output = len(set([row[-1] for row in train_data]))  # output only 2 classes 1 or 0

neurons_in_each_layer = gui_obj.number_of_neurons
hidden_layers = gui_obj.number_of_hidden_layer
activation_choice = gui_obj.type_activatio_function
learning_rate = gui_obj.learning_rate
n_epoch = gui_obj.number_of_epoach
bias = int(gui_obj.add_bais)

test_output = [row[-1] for row in test_data]

network = initialize_weights(neurons_input, hidden_layers, neurons_in_each_layer, neurons_output)  # random weights for 2 hidden layers
train_network(network, train_data, learning_rate, n_epoch, neurons_output, activation_choice, bias)

predicted_result = test(network, test_data, activation_choice, bias)
confusion_matrix, gui_obj.accuracy = accuracy(predicted_result, test_data)
#------------ print output----------------#
#weights
for layer in network:
    print(layer)
gui_obj.accuracy*=100
print("Final accuracy =", gui_obj.accuracy, "%")
#Confusion Matrix
#          predicted_0      predicted_1     predicted_2     total
# actual_0                                                 total_actual_0
# actual_1                                                 total_actual_1
# actual_2                                                 total_actual_2
# total     total_pred_0    total_pred_1    total_pred_2
print("               #--- Confusion Matrix ---#")
print("          predicted_0      predicted_1     predicted_2     total")
print(" actual_0                                                 total_actual_0")
print(" actual_1                                                 total_actual_1")
print(" actual_2                                                 total_actual_2")
print(" total     total_pred_0    total_pred_1    total_pred_2")

[print(confusion_matrix[i]) for i in range(4)]
#for i in range(4):
 #   print("actual_"+str(i),confusion_matrix[i], "total_actual_"+str(i))
gui_obj.Display_accuracy()

window.mainloop()

