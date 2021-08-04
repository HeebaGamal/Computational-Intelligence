import numpy as np
import matplotlib.pyplot as plt

import readFromFile as rf
import DivideData as DivDa
import DrawHelper as dhelper
import DrawData as ddata
class Traning:
    #_W = np.random.rand(len, hei)
    _W=None
    tran_x1_F1 = []
    tran_x2_F1 = []
    tran_x1_F2 = []
    tran_x2_F2 = []


    #def calulateAcuricyFun(self):


    @classmethod
    def signumClasFun(self, _Z):
        return np.where(_Z >=0.0 ,1,-1)
    def activatoinFun(self,X):
        return np.dot(self._W[0][1:].T,X)+self._W[0][0]
    @classmethod
    def testFun(self,_W , b  , n , _Xtest,_Ytest):
        err1 = 0
        err2=0

        cou=0

        #print("Count 1 = {}".format(cou))
        for x, y in zip(_Xtest, _Ytest):

            _Z = self.activatoinFun(self, x)
            _A = Traning.signumClasFun(_Z)

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
    def traningFun(self, b, m, n, _Xtrain, _Ytrain):
        len,hei=_Xtrain.shape
        self._W=np.random.rand(1,1 + hei)
        self._W[0][0]=b
        self.train_errors_ = []

        for i in range(m):
            err=0
            for x,y in zip(_Xtrain , _Ytrain):
                _Z=self.activatoinFun(self,x)
                _A=Traning.signumClasFun(_Z)
                _L= y - _A
                if y == 1:
                  self.tran_x1_F1.append(x[0])
                  self.tran_x2_F1.append(x[1])
                else:
                    self.tran_x1_F2.append(x[0])
                    self.tran_x2_F2.append(x[1])
                update=(n*_L)
                self._W[0][1:]+=(update* x)
                self._W[0][0]+=update
                err+=int(update != 0)
            self.train_errors_.append(err)


        return _L,self._W , _A , self.train_errors_
    @classmethod
    def calMinMaxInArray(self,array):
        return np.min(array),np.max(array)
    @classmethod
    def run(self, _F1, _F2, _C1, _C2, n, m, b):
        filename = 'IrisData.txt'

        x1, x2, x3, x4, y, header = rf.SplitData.fillArray(filename)
        feature1 = "X1"
        feature2 = "X2"
        feature3 = "X3"
        feature4 = "X4"
        featureDic = {feature1: x1, feature2: x2, feature3: x3, feature4: x4}

        # find min and max val for draw lin
        _minX1, _maxX1 = Traning.calMinMaxInArray(x1)
        _minX2, _maxX2 = Traning.calMinMaxInArray(x2)
        _minX3, _maxX3 = Traning.calMinMaxInArray(x3)
        _minX4, _maxX4 = Traning.calMinMaxInArray(x4)
        minmaxFeatureDic = {feature1: [_minX1, _maxX1],
                            feature2: [_minX2, _maxX2],
                            feature3: [_minX3, _maxX3],
                            feature4: [_minX4, _maxX4]}

        _minX1 = np.min(x1)
        _maxX1 = np.max(x1)

        # show scatter fig
        dhelper.DrawHelper.DrawDataScatter(x1, x2, x3, x4, feature1, feature2, feature3, feature4)

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
        _xtran, _ytrain, _xtest, _ytest = DivDa.DivideData.dividData(_X, _Y, _r1, _r2)

        _L, _W, _A, train_errors_list = Traning.traningFun(b, m, n, _xtran, _ytrain)
        print('Weight ={}'.format(_W))
        # (0===>x1) , (max ==>X2),
        _xPointLine = [0, -1 * (_W[0][2] * float(minmaxFeatureDic[_F1][1]) + b) / _W[0][1]]
        _yPointLine = [-1 * (_W[0][1] * 0 + b) / _W[0][2], minmaxFeatureDic[_F2][1]]


        # 0 ==>F1
        tempXP1 = 0
        tempYP1 = -1 * (b) / _W[0][2]

        # max==>F2
        tempXP2 = -1 * (_W[0][2] * float(minmaxFeatureDic[_F1][1]) + b) / _W[0][1]
        tempYP2 = float(minmaxFeatureDic[_F2][1])

        # max ==>F1
        tempXP3 = float(minmaxFeatureDic[_F1][1])
        tempYP3 = -1 * (_W[0][1] * float(minmaxFeatureDic[_F1][1]) + b) / _W[0][2]
        # min ===>F2
        tempXP4 = -1 * (_W[0][2] * float(minmaxFeatureDic[_F2][0]) + b) / _W[0][1]
        tempYP4 = float(minmaxFeatureDic[_F2][0])

        # min ==> F1
        tempYP5 = -1 * (_W[0][1] * float(minmaxFeatureDic[_F1][0]) + b) / _W[0][2]
        tempXP5 = float(minmaxFeatureDic[_F1][0])

        # 0===>F2
        tempXP6 = -1 * (b) / _W[0][1]
        tempYP6 = 0



        Cdraw = ddata.DrawData([self.tran_x1_F1, self.tran_x1_F2 ],
                               [self.tran_x2_F1,self.tran_x2_F2],
                               _F1, _F2, "fig-{}-{}-{}-{}".format(_C1, _C2, _F1, _F2))



        _xvaLine=np.array([tempXP3, tempXP1])
        _yvaLine=np.array([tempYP3 , tempYP1])

        Cdraw.xLine=_xvaLine
        Cdraw.yLine=_yvaLine


        Cdraw.scatterplotFun(_xvaLine,_yvaLine)


        err1, err2, cl1Cou = Traning.testFun(_W, b, n, _xtest, _ytest)
        EvaluationMat = [[cl1Cou - err1, err1], [err2, 40 - cl1Cou - err2]]
        accurcy = (cl1Cou - err1 + 40 - cl1Cou - err2) / 40

        print("errors in  {} = {} , errors in {} = {}".format(_C1,err1,_C2, err2))
        print('confusion matrix = {}'.format(EvaluationMat))
        print('accurcy = {} %'.format(accurcy*100))
        print()
    @classmethod
    def abline(self,slope, intercept,minF1,maxF1):
        """Plot a line from slope and intercept"""
        axes = plt.gca( )
        x_vals = np.array(axes.get_xlim())
        y_vals = intercept + slope * x_vals
        #plt.plot(x_vals, y_vals, '--')
        return x_vals , y_vals
if __name__ == '__main__':
    b=1
    feature1 = "X1"
    feature2 = "X2"
    feature3 = "X3"
    feature4 = "X4"
    cl1 = "Iris-setosa"  # r1=0
    cl2 = "Iris-versicolor"  # r2=1
    cl3 = "Iris-virginica"  # r3=2

    _F1="X1"
    _F2="X2"
    _C1=cl1
    _C2=cl2
    n = 0.00001
    m = 500
    Traning.run(_F1,_F2,_C1,_C2,n,m,b)
