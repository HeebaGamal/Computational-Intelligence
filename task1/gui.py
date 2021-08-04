from tkinter import *
from functools import partial
import task1 as t1
import adaline as ada
master = Tk()
master.geometry("700x200")


classlLable=Label(master,text="class (choose 2 classes):   ").grid(row=0,column=0,sticky=W)
class1 = IntVar()
Checkbutton(master, text="class1", variable=class1).grid(row=0,column=1, sticky=W)
class2 = IntVar()
Checkbutton(master, text="class2", variable=class2).grid(row=0,column=2, sticky=W)
class3 = IntVar()
Checkbutton(master, text="class3", variable=class3).grid(row=0,column=3, sticky=W)

classlLable=Label(master,text="features  (choose 2 features):   ").grid(row=4,column=0,sticky=W)
feature1 = IntVar()
Checkbutton(master, text="feature 1", variable=feature1).grid(row=4,column=1, sticky=W)
feature2 = IntVar()
Checkbutton(master, text="feature 2", variable=feature2).grid(row=4,column=2, sticky=W)
feature3 = IntVar()
Checkbutton(master, text="feature 3", variable=feature3).grid(row=4,column=3, sticky=W)
feature4 = IntVar()
Checkbutton(master, text="feature 4", variable=feature4).grid(row=4,column=4, sticky=W)

classlLable=Label(master,text="enter learning rate eta:   ").grid(row=6,column=0,sticky=W)
eta=StringVar(master)
eta.set('0.1')
entry1 = Entry(master,textvariable=eta).grid(row=6,column=1,sticky=W)

classlLable=Label(master,text="enter thershold:   ").grid(row=7,column=0,sticky=W)
thershold=StringVar(master)
thershold.set('0.1')
entry3 = Entry(master,textvariable=thershold).grid(row=7,column=1,sticky=W)

classlLable=Label(master,text="enter number of iteration m :   ").grid(row=8,column=0,sticky=W)
m=IntVar(master)

entry2 = Entry(master,textvariable=m).grid(row=8,column=1,sticky=W)

bias=Label(master,text="add bias or not   ").grid(row=10,column=0,sticky=W)
bias = IntVar()
Checkbutton(master, text="bias", variable=bias).grid(row=10,column=1, sticky=W)


def callback2(class1 ,class2 ,class3 ,feature1,feature2,feature3,feature4,eta,m, bias,thershold):

    _Cl1=None
    _Cl2=None
    _Feat1=None
    _Feat2=None
    _n=float(eta.get())
    _m=m.get()
    _b=bias.get()
    _thershold=float(thershold.get())
    if class1.get() == 1:
        if _Cl1 == None:
            _Cl1 = 'Iris-setosa'
        elif _Cl2 == None:
            _Cl2 = 'Iris-setosa'
    if class2.get() == 1:
        if _Cl1 == None:
            _Cl1 = 'Iris-versicolor'
        elif _Cl2 == None:
            _Cl2 = 'Iris-versicolor'
    if class3.get() == 1:
        if _Cl1 == None:
            _Cl1 = 'Iris-virginica'
        elif _Cl2 == None:
            _Cl2 = 'Iris-virginica'

    if feature1.get() == 1:
        if _Feat1 == None:
            _Feat1 = 'X1'
        elif _Feat2 == None:
            _Feat2 = 'X1'
    if feature2.get() == 1:
        if _Feat1 == None:
            _Feat1 = 'X2'
        elif _Feat2 == None:
            _Feat2 = 'X2'
    if feature3.get() == 1:
        if _Feat1 == None:
            _Feat1 = 'X3'
        elif _Feat2 == None:
            _Feat2 = 'X3'
    if feature4.get() == 1:
        if _Feat1 == None:
            _Feat1 = 'X4'
        elif _Feat2 == None:
            _Feat2 = 'X4'
    #T1=t1.Traning()
    #T1.run(_Feat1,_Feat2,_Cl1,_Cl2,_n,_m,_b,_thershold)
    Ada=ada.Traning()
    Ada.run(_Feat1,_Feat2,_Cl1,_Cl2,_n,_m,_b,_thershold)



callback = partial(callback2,class1 ,class2 ,class3 ,feature1,feature2,feature3,feature4,eta,m, bias,thershold)
B =Button(master, text ="submit", command = callback).grid(row=15,column=3, sticky=W)

master.mainloop()