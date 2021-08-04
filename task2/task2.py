import numpy as np
import matplotlib.pyplot as plt
import readFromFile as rf
import DivideData as DivDa
import DrawHelper as dhelper
import DrawData as ddata
class Adaline:

    n_m=None
    bb=0
    #def calulateAcuricyFun(self):


    @classmethod
    def signumClasFun(self, _Z):
        return np.where(_Z >=0.0 ,1,-1)
    def activatoinFun(self,X,mm,bb):
        return np.dot(X,mm)+bb
    @classmethod
    def testFun(self , _Xtest,_Ytest):
        err1 = 0
        err2=0
        cou=0
        leng,hei = _Xtest.shape
        _Xtest=np.insert(_Xtest,0,np.ones(leng),axis=1)

        for x, y in zip(_Xtest, _Ytest):
            n_X = np.array([x[1], x[2]])
            _Z = self.activatoinFun(self,n_X,self.n_m,self.bb)
            _A = Adaline.signumClasFun(_Z)

            if y == 0:
                print('EXPtion')
            if y== 1:
                cou+=1
                if y != _A :
                    err1 += 1

            if y!= _A and y== -1:
                err2+=1

        return err1,err2,cou
    @classmethod
    def traningFun(self, b, n, _Xtrain, _Ytrain , threshold,m):
        leng,hei=_Xtrain.shape

        self.train_errors_ = []

        self.n_m = np.random.rand(2, 1)
        self.bb = b

        #one_arr=np.ones(leng)
        _Xtrain=np.insert(_Xtrain,0,np.ones(leng),axis=1)
        iteration=1;
        while True:
            err=0
            for x,y in zip(_Xtrain , _Ytrain):
                n_X = np.array([x[1], x[2]])
                _Z=self.activatoinFun(self,n_X,self.n_m,self.bb)
                _A=_Z
                _L= y - _A
                new_x = n_X.reshape(2, 1)
                self.n_m = self.n_m + (n * _L * new_x)
                self.bb = self.bb + (n * _L)

            errC1=0
            errC2=0
            self.final_train_error = []
            for x,y in zip(_Xtrain,_Ytrain):
                n_X = np.array([x[1], x[2]])
                _z=self.activatoinFun(self,n_X,self.n_m,self.bb)
                self.final_train_error.append(y - _z)
                if _z != y and y==1:
                    errC1+=1
                if _z!= y and y==-1:
                    errC2+=1

            MSE=1/(len(self.final_train_error) * 2) * np.sum([x**2 for x in self.final_train_error])
            print("MSE = {}".format(MSE))
            if MSE < threshold or iteration > m:
                break
            iteration+=1
            #TODO calculate MSE and beark codation

        print("MSe ={}".format(MSE))
        return _L,  _A , self.train_errors_,self.n_m,self.bb
    @classmethod
    def calMinMaxInArray(self,array):
        return np.min(array),np.max(array)
    @classmethod
    def run(self, _F1, _F2, _C1, _C2, n, b , threshold,m):
        filename = 'IrisData.txt'

        x1, x2, x3, x4, y, header = rf.SplitData.fillArray(filename)

        x1=x1/np.linalg.norm(x1)
        x2=x2/np.linalg.norm(x2)
        x3=x3/np.linalg.norm(x3)
        x4=x4/np.linalg.norm(x4)


        feature1 = "X1"
        feature2 = "X2"
        feature3 = "X3"
        feature4 = "X4"
        featureDic = {feature1: x1, feature2: x2, feature3: x3, feature4: x4}

        # find min and max val for draw lin
        _minX1, _maxX1 = Adaline.calMinMaxInArray(x1)
        _minX2, _maxX2 = Adaline.calMinMaxInArray(x2)
        _minX3, _maxX3 = Adaline.calMinMaxInArray(x3)
        _minX4, _maxX4 = Adaline.calMinMaxInArray(x4)
        minmaxFeatureDic = {feature1: [_minX1, _maxX1],
                            feature2: [_minX2, _maxX2],
                            feature3: [_minX3, _maxX3],
                            feature4: [_minX4, _maxX4]}

        _minX1 = np.min(x1)
        _maxX1 = np.max(x1)

        # show scatter fig
        #dhelper.DrawHelper.DrawDataScatter(x1, x2, x3, x4, feature1, feature2, feature3, feature4)

        cl1 = "Iris-setosa"  # r1=0
        cl2 = "Iris-versicolor"  # r2=1
        cl3 = "Iris-virginica"  # r3=2

        clDic = {cl1: 0, cl2: 1, cl3: 2}
        # input from user

        _r1 = 0
        _r2 = 1

        # _X = rf.SplitData._Xmatrix(b, x1, x2, x3, x4,_F1,_F2, header )
        _X = rf.SplitData._Xmatrix2(x1, x2, x3, x4, _F1, _F2, header)

        _Y = rf.SplitData.convertYMat(y, _C1, _C2)
        #_xtran, _ytrain, _xtest, _ytest = DivDa.DivideData.dividArray(_X, _Y, _r1, _r2)
        _xtr , _ytr ,_xtran, _ytrain, _xtest, _ytest = DivDa.DivideData.dividData(_X, _Y, _r1, _r2)

        _L, _A, train_errors_list,n_m,bb = Adaline.traningFun(b, n, _xtran, _ytrain , threshold,m)
        print('Weight ={}'.format(n_m))


        # 0 ==>F1
        tempXP1 = 0
        tempYP1 = -1 * (bb) / n_m[1]


        # max ==>F1
        tempXP3 = float(minmaxFeatureDic[_F1][1])
        tempYP3 = -1 * (n_m[0]* float(minmaxFeatureDic[_F1][1]) + bb) / n_m[1]

        Cdraw = ddata.DrawData([_xtr[:30,[0]] , _xtr[30:60 , [0]]],
                               [_xtr[:30,[1]] ,_xtr[30:60 , [1]] ],
                               _F1, _F2, "fig-{}-{}-{}-{}".format(_C1, _C2, _F1, _F2))

        _xvaLine=np.array([tempXP1 , tempXP3])

        _yvaLine=np.array([tempYP1 , tempYP3])

        Cdraw.xLine=_xvaLine
        Cdraw.yLine=_yvaLine


        Cdraw.scatterplotFun(_xvaLine,_yvaLine)


        err1, err2, cl1Cou = Adaline.testFun( _xtest, _ytest)
        EvaluationMat = [[cl1Cou - err1, err1], [err2, 40 - cl1Cou - err2]]
        accurcy = (cl1Cou - err1 + 40 - cl1Cou - err2) / 40

        print("errors in  {} = {} , errors in {} = {}".format(_C1,err1,_C2, err2))
        print('EvaluationMat = {}'.format(EvaluationMat))
        print('accurcy using Adaline = {} %'.format(accurcy*100))
        print()
if __name__ == '__main__':
    b=1
    feature1 = "X1"
    feature2 = "X2"
    feature3 = "X3"
    feature4 = "X4"
    cl1 = "Iris-setosa"  # r1=0
    cl2 = "Iris-versicolor"  # r2=1
    cl3 = "Iris-virginica"  # r3=2

    _F1="X2"
    _F2="X4"
    _C1=cl1
    _C2=cl2
    n = 0.001
    m = 500
    threshold=0.1

    Adaline.run(_F1, _F2, _C1, _C2, n, b,threshold,m)
