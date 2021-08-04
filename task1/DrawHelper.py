import DrawData as ddata

class DrawHelper:

    @classmethod
    def DrawDataScatter(self, x1, x2, x3, x4, lable1, lable2, lable3, lable4):
        Cdraw=ddata.DrawData([x1[:50],x1[50:100] , x1[100:]],[ x2[:50],x2[50:100] , x2[100:] ] , lable1 , lable2 , "figure1-{}-{}".format(lable1,lable2))
        Cdraw.scatterFun()
        Cdraw=ddata.DrawData([x1[:50],x1[50:100] , x1[100:]],[ x3[:50],x3[50:100] , x3[100:] ] , lable1 , lable3 , "figure1-{}-{}".format(lable1,lable3))
        Cdraw.scatterFun()
        Cdraw=ddata.DrawData([x1[:50],x1[50:100] , x1[100:]],[ x4[:50],x4[50:100] , x4[100:] ] , lable1 , lable4 , "figure1-{}-{}".format(lable1,lable4))
        Cdraw.scatterFun()
        Cdraw=ddata.DrawData([x2[:50],x2[50:100] , x2[100:]],[ x3[:50],x3[50:100] , x3[100:] ] , lable2 , lable3 , "figure1-{}-{}".format(lable2,lable3))
        Cdraw.scatterFun()
        Cdraw=ddata.DrawData([x2[:50],x2[50:100] , x2[100:]],[ x4[:50],x4[50:100] , x4[100:] ] , lable2 , lable4 , "figure1-{}-{}".format(lable2,lable4))
        Cdraw.scatterFun()
        Cdraw=ddata.DrawData([x3[:50],x3[50:100] , x3[100:]],[ x4[:50],x4[50:100] , x4[100:] ] , lable3 , lable4 , "figure1-{}-{}".format(lable3,lable4))
        Cdraw.scatterFun()


