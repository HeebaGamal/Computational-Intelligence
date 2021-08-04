import numpy as np
import pandas as pd


class ReadFromFile:
    @classmethod
    def OpReadData(self,fileName ):
        my_file = open(fileName, "r")
        filedata=my_file.read()
        return filedata


class SplitData:
    X1=[]
    X2=[]
    X3=[]
    X4=[]
    Y=[]
    @classmethod
    def fillArray(self,filename):
        data = pd.read_csv(filename, sep=",", header=None)
        data.columns = ["X1", "X2", "X3", "X4","Class"]
        cl1="X1"
        cl2="X2"
        cl3="X3"
        cl4="X4"
        header=[]
        header.append(cl1)
        header.append(cl2)
        header.append(cl3)
        header.append(cl4)
        x1=data[cl1]
        x2=data[cl2]
        x3=data[cl3]
        x4=data[cl4]
        y = data["Class"]
        x1=self.convertToNPArray(self ,x1[1:])
        x2=self.convertToNPArray(self ,x2[1:])
        x3=self.convertToNPArray(self,x3[1:])
        x4=self.convertToNPArray(self,x4[1:])
        y=self.convertToNPArray(self,y[1:])
        #return  x1,x2,x3,x4,y,header
        return [float(temp) for temp in x1] , [float(temp) for temp in x2] , [float(temp) for temp in x3] ,[float(temp) for temp in x4] , y ,header

    @staticmethod
    def convertToNPArray(self,array):
        return np.array(array)
    @classmethod
    def _Xmatrix(self,x0,x1,x2,x3,x4 , cl1 , cl2 , data):
        if cl1 not in data or cl2 not in data :
            print("Exc ")


        _X=np.empty([len(x1),3])
        for i in range(len(x1)):
            temp=np.empty([1,3])
            #temp=np.empty([1,3])
            #print(temp)
            #print(temp.shape)
            #temp.append(x0)
            _i=0
            temp[_i]=x0
            _i+=1
            if cl1 == "X1" or cl2 == "X1":
                temp[0][_i]=x1[i]
                _i+=1
                #temp.append(x1[i])
            if cl1 == "X2" or cl2 == "X2":
                temp[0][_i] =x2[i]
                _i+=1
                #temp.append(x2[i])

            if cl1 == "X3" or cl2 == "X3":
                temp[0][_i]= x3[i]
                _i+=1
                #temp.append(x3[i])

            if cl1 == "X4" or cl2 == "X4":
                temp[0][_i] =x4[i]
                _i+=1
            _X[i]=temp

        return (np.array(_X))



    @classmethod
    def _Xmatrix2(self, x1, x2, x3, x4, cl1, cl2, data):
        if cl1 not in data or cl2 not in data:
            print("Exc ")


        _X = np.empty([len(x1), 2])
        for i in range(len(x1)):
            temp = np.empty([1, 2])

            _i = 0

            if cl1 == "X1" or cl2 == "X1":
                temp[0][_i] = x1[i]
                _i += 1
                # temp.append(x1[i])
            if cl1 == "X2" or cl2 == "X2":
                temp[0][_i] = x2[i]
                _i += 1
                # temp.append(x2[i])

            if cl1 == "X3" or cl2 == "X3":
                temp[0][_i] = x3[i]
                _i += 1
                # temp.append(x3[i])

            if cl1 == "X4" or cl2 == "X4":
                temp[0][_i] = x4[i]
                _i += 1

            _X[i] = temp
        #print(_X)
        return (np.array(_X))
    @classmethod
    def convertYMat(self,y,cl1,cl2):
        _Y=[]
        for i in range(len(y)):
            if(y[i] == cl1):
                _Y.append(1)
            elif y[i]== cl2:
                _Y.append(-1)
            else:
                _Y.append(0)
        return _Y


'''
if __name__ == '__main__':
    filename='IrisData.txt'
    x1 , x2 , x3 ,x4 , y, header=SplitData.fillArray(filename)
    _X = SplitData._Xmatrix(1,x1,x2,x3,x4,"X1","X2",header)
    print(_X)
'''

