from math import exp
from random import seed
from random import random
from tkinter import *
from tkinter.messagebox import *
from tkinter import ttk
import tkinter as tk
from functools import partial


class GUI:
    number_of_epoach = 0
    number_of_hidden_layer = 0
    learning_rate = 0.0
    number_of_neurons = []
    type_activatio_function = None
    add_bais = '0'
    accuracy = 0.0
    def __init__(self, window):
        self.window = window
    def Take_input(self, n_of_eochs, n_of_hidden_layer, learning_rate, number_of_neurans, cmb_Activation_function, lbl_add_bias):
        self.number_of_epoach       = int(n_of_eochs.get())
        self.number_of_hidden_layer = int(n_of_hidden_layer.get())
        self.learning_rate          = float(learning_rate.get())
        temp_no_neurans = str(number_of_neurans.get()).split(',')

        for i in range(len(temp_no_neurans)):
            temp_no_neurans[i] = int(temp_no_neurans[i])

        self.number_of_neurons = temp_no_neurans
        self.type_activatio_function = cmb_Activation_function.get()
        self.add_bais = str(lbl_add_bias.get())


    def GUI_input(self):
        font = ('Verdana', 13, 'bold')
        self.window.title('Abigail')
        self.window.geometry('550x350')
        self.window['background']='#660066'

        #number_of_epochs
        lbl_number_of_epochs = Label(self.window, text="number of epochs : ",font=font,bg='#660066').grid(row=0, column=0, sticky=W)
        n_of_eochs = IntVar(self.window)
        n_of_eochs.set(100)
        txt_number_of_epochs = Entry(self.window, textvariable=n_of_eochs, font=font).grid(row=0, column=1, sticky=W)

        hmmmmmmm = Label(self.window, text="               ",bg='#660066').grid(row=1, column=1, sticky=W)

        #hidden layer
        lbl_hidden_layer= Label(self.window, text="number hidden layer : ", font=font,bg='#660066').grid(row=2, column=0, sticky=W)
        n_of_hidden_layer = IntVar(self.window)
        n_of_hidden_layer.set(3)
        txt_hidden_layer = Entry(self.window, textvariable=n_of_hidden_layer, font=font).grid(row=2, column=1, sticky=W)

        hmmmmmmm = Label(self.window, text="               ",bg='#660066').grid(row=3, column=1, sticky=W)

        # learning_rate
        lbl_learning_rate = Label(self.window, text="number learning rate : ", font=font,bg='#660066').grid(row=4, column=0, sticky=W)
        learning_rate = StringVar(self.window)
        learning_rate.set(0.01)
        txt_learning_rate = Entry(self.window, textvariable=learning_rate, font=font).grid(row=4, column=1, sticky=W)

        hmmmmmmm = Label(self.window, text="               ",bg='#660066').grid(row=5, column=1, sticky=W)

        # number_of_neurans
        lbl_number_of_neurans = Label(self.window, text="number of neurons : ", font=font,bg='#660066').grid(row=6, column=0, sticky=W)
        number_of_neurans = StringVar(self.window)
        number_of_neurans.set("5, 7, 10")
        txt_number_of_neurans = Entry(self.window, textvariable=number_of_neurans, font=font).grid(row=6, column=1, sticky=W)

        #print(type(number_of_neurans))
        hmmmmmmm = Label(self.window, text="               ",bg='#660066').grid(row=7, column=1, sticky=W)

        # Combobox Activation function
        lbl_Activation_function = Label(self.window, text="Activation function : ", font=font,bg='#660066').grid(row=8, column=0, sticky=W)

        n = StringVar(self.window)
        cmb_Activation_function = ttk.Combobox(self.window, width = 23, textvariable = n, font=font)

        cmb_Activation_function['values'] = (' sigmoid', 'Tangent sigmoid ')

        cmb_Activation_function.grid(row = 8, column = 1)
        cmb_Activation_function.current(1)

        hmmmmmmm = Label(self.window, text="               ",bg='#660066').grid(row=9, column=1, sticky=W)

        #Add bias
        lbl_add_bias = Label(self.window, text="Add Bias : ", font=font,bg='#660066').grid(row=10, column=0, sticky=W)
        lbl_add_bias = StringVar()
        lbl_add_bias.set('0')

        Checkbutton(self.window, text="bias", variable=lbl_add_bias, font =font,bg='#ffffaa').grid(row=10, column=1, sticky=W)

        hmmmmmmm = Label(self.window, text="               ",bg='#660066').grid(row=11, column=1, sticky=W)

        #btn_take input
        take_input_partial = partial(self.Take_input, n_of_eochs, n_of_hidden_layer,
                                     learning_rate, number_of_neurans, cmb_Activation_function,
                                     lbl_add_bias)

        btn_take_input = Button(self.window, text="Calculate", command = take_input_partial, font=('Verdana', 21, 'bold')).grid(row=12, column=1, sticky=W)

    def Display_accuracy(self):
        tk.messagebox.showinfo(title='Final Accurecy', message=str(self.accuracy)+"%")


