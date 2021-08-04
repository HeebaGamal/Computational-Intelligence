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

''' 
if __name__ == '__main__':
    x=[[1,2,3,4],[1,2,3,4]]
    y=[[10,20,30,40],[15,22,31,94]]
    _x=[1,2,3,4]
    _y=[1,35,18,48]
    _a=[0,10,20]
    _b=[0,10,20]
    _z=[1,2,3,4]
    _c=[15,22,31,94]
    plt.figure('fig1')
    #plt.scatter(x,y) to draw points with x,y  as point on axis
    #plt.plot(_a,_b)

    plt.scatter(_x,_y)
    plt.scatter(_z, _c )
    plt.plot(_a,_b)

    #use plt.plot(x,y) to draw line with x,y as point on axis
    #plt.plot()
    #CDraw=DrawData(x,y,'Value','Squ','fig1')
    #CDraw.scatterFun()
    #CDraw.plotFun()
    plt.show()
    Dict = {1: ["aaaa","bbbb"], 2: 'For', 3: 'Geeks'}
    print(Dict[1][0])
'''