import numpy as np
import random as rn
'''        subSet=_X[:50]
        _Xtrain=np.random.choice(subSet[0], size=30,replace=False)
        print("@@@@@@@@@@@@2")
        print(_Xtrain)

        np.random.shuffle()

        subset = rn.sample(_X[50:], 30)
        _Xtrain.append(temp)

        _Xtest=rn.sample(_X[:50],20)

        temp=rn.sample(_X[50:],20)
        _Xtest.append(temp)

        _Ytrain=rn.sample(_Y[:50],30)
        _Ytest=rn.sample(_Y[:50],20)
        temp=rn.sample(_Y[50:],30)
        _Ytrain.append(temp)
        temp=rn.sample(_ْY[50:],20)
        _Ytest.append(temp)
'''


class DivideData:
    @classmethod
    def dividArray(self,_Xma , _Yma,r1,r2):
        #60% for traning and 40% for test
        #print(_X[:50])

        #Merge data
        Data=DivideData.mergeDataElement(_Xma,_Yma)
        np.random.shuffle(Data)
        #_len,_hei=_Xma.shape
        lenght, het = Data.shape
        DataMat = np.empty([100, het ])
        _X=np.empty([100,het-1])
        _Y=np.empty([100,1])
        #print(np.where( Data[0][2] == 0 , 1 , 2))
        _i=0
        for i in range(lenght):
            if Data[i][2] != 0.0 :
                #print("in IF ")
                #DataMat[_i]=Data[i]
                _X[_i]=Data[i][:2]
                _Y[_i]=Data[i][2:][0]
                #print(Data[i][:2])
                #print('y= {}',Data[i][2:][0])
                #te=Data[i][2:][0]
                _i+=1
        '''_len,_hei=_Xma.shape
        #print(DataMat[:])
        _X = DataMat[:][:_hei]
        _Y = DataMat[:][_hei]'''

        _Xtrain=_X[(r1*50):(50*r1)+30]
        _Xtest=_X[50*r1+30:(50*r1)+50]
        _Xtrain= np.vstack((_Xtrain,_X[(50*r2):(50*r2)+30]))
        #print(_Xtrain)

        _Xtest=np.vstack((_Xtest, _X[(50*r2)+30:(50*r2)+50]))
        #_Xtrain.append(_X[50:80])
        #_Xtest.append(_X[80:])

        _Ytrain = _Y[(r1*50):(50*r1)+30]
        _Ytest = _Y[(50*r1)+30:(50*r1)+50]
        #_Ytrain.append(_Y[50:80])
        #_Ytest.append(_Y[80:])
        _Ytrain= np.append(_Ytrain,_Y[(50*r2):(50*r2)+30])
        _Ytest= np.append(_Ytest,_Y[(50*r2)+30:(50*r2)+50])


        return np.array(_Xtrain) , np.array(_Ytrain) , np.array(_Xtest) , np.array(_Ytest)

    @classmethod
    def dividData(self,_Xma , _Yma ,r1,r2):
        Data = DivideData.mergeDataElement(_Xma, _Yma)
        Cl1=Data[:50][:]
        Cl2=Data[50:100][:]
        Cl3=Data[100:][:]
        np.random.shuffle(Cl1)
        np.random.shuffle(Cl2)
        np.random.shuffle(Cl3)
        Data=Cl1
        Data=np.vstack((Data , Cl2))
        Data=np.vstack((Data,Cl3))
        #np.random.shuffle(Data)
        lenght, het = Data.shape
        _X = np.empty([102, het - 1])
        _Y = np.empty([102, 1])
        _i = 0
        for i in range(lenght):
            if Data[i][2] != 0.0:
                _X[_i] = Data[i][:2]
                _Y[_i] = Data[i][2:][0]
                _i += 1
        _Xtrain=_X[(r1*50):(50*r1)+30]
        _Xtest=_X[50*r1+30:(50*r1)+50]
        _Xtrain= np.vstack((_Xtrain,_X[(50*r2):(50*r2)+30]))
        #print(_Xtrain)

        _Xtest=np.vstack((_Xtest, _X[(50*r2)+30:(50*r2)+50]))
        #_Xtrain.append(_X[50:80])
        #_Xtest.append(_X[80:])

        _Ytrain = _Y[(r1*50):(50*r1)+30]
        _Ytest = _Y[(50*r1)+30:(50*r1)+50]
        #_Ytrain.append(_Y[50:80])
        #_Ytest.append(_Y[80:])
        _Ytrain= np.append(_Ytrain,_Y[(50*r2):(50*r2)+30])
        _Ytest= np.append(_Ytest,_Y[(50*r2)+30:(50*r2)+50])
        _XtrainWithoutSh=_Xtrain
        _YtrainWithoutSh = _Ytrain
        traingData = DivideData.mergeDataElement(_Xtrain,_Ytrain )
        #print(traingData[:30 , [0,2]])

        np.random.shuffle(traingData)
        len2,he2 = traingData.shape
        for i in range(len2):
            _Xtrain[i] = traingData[i][:2]
            _Ytrain[i] = traingData[i][2:][0]
        return np.array(_XtrainWithoutSh),np.array(_YtrainWithoutSh), np.array(_Xtrain) , np.array(_Ytrain) , np.array(_Xtest) , np.array(_Ytest)
    @classmethod
    def mergeDataElement(self,_Xmat,_Ymat):
        lenght,het=_Xmat.shape
        DataMat=np.empty([lenght,het+1])
        for i in range(len(_Ymat)):
            arr=np.append(_Xmat[i],_Ymat[i])
            #DataMat=np.vstack((DataMat,arr))
            DataMat[i]=arr
        return DataMat

