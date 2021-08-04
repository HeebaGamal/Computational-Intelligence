import matplotlib.pyplot as plt

class DrawData:

    def __init__(self,x,y,xLable,yLable,figureName):
        '''

        :param x: 2d array each row as array like [[1,2,3,4],[8,2,3,10]] ==>[1,2,3,4] for fist scatter and [8,2,3,10] for another scctter
        :param y:
        :param xLable:
        :param yLable:
        :param figureName:
        '''
        self.xSca=x
        self.ySca=y
        self.xLable=xLable
        self.yLable=yLable
        self.figureName=figureName
        self.xLine=None
        self.yLine=None
    def filldata(self):
        plt.figure(self.figureName)
        plt.xlabel(self.xLable)
        plt.ylabel(self.yLable)
    #@staticmethod
    def scatterFun(self):
        self.filldata()
        for _x , _y in zip(self.xSca , self.ySca):
            plt.scatter(_x, _y)
        plt.show()
    def plotFun(self):
        self.filldata()
        plt.plot(self.xLine, self.yLine,color='red', linewidth=3)
        plt.show()
    def scatterplotFun(self,xL,yL):
        self.filldata()
        self.xLine = xL
        self.yLine = yL
        plt.plot(self.xLine, self.yLine,color='red', linewidth=3)
        for _x, _y in zip(self.xSca, self.ySca):
            plt.scatter(_x, _y)

        plt.show()

