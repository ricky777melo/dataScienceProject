import matplotlib.pyplot as plt
import numpy as np
import os
cur_path =  os.path.abspath(os.path.dirname(__file__))
root_path = cur_path[:cur_path.find("pyHFT\\")+len("pyHFT\\")]

def printList(array,dim=2):
    if dim==2:
        for i in array:
            print(i)
    if dim==1:
        print(array)
def curve(title,x,y,label='first',x1=[],y1=[],label1='second',x2=[],y2=[],label2='third',x3=[],y3=[],label3='forth',prompt="曲线如图所示"):
    #网格
    ax = plt.gca()
    ax.set_xlim(0, x.__len__())
    miloc = plt.MultipleLocator(1)
    ax.xaxis.set_minor_locator(miloc)
    ax.grid(axis='x', which='minor')
    #网格

    plt.plot(x,y,label=label)
    plt.plot(x1,y1,label=label1)
    plt.plot(x2,y2,label=label2)
    plt.plot(x3,y3,label=label3)
    plt.title(title)
    plt.legend()

    plt.show()
    print()
    print(title,prompt)

def threeD(xd,yd,zd,Xlabel='x',Ylabel='y',Zlabel='z'):
    xd=np.array(xd)
    yd=np.array(yd)
    zd=np.array(zd)
    fig = plt.figure()
    ax1 = plt.axes(projection='3d')
#    ax1.set_zlim3d(0.5,0.6)设置z轴的显示范围
#    ax1.set_ylim3d(10,20)
    ax1.scatter3D(xd, yd, zd, cmap='Blues')  # 绘制散点图
    plt.xlabel(Xlabel)
    plt.ylabel(Ylabel)
    plt.show()
def progressBar(time,times,prompt="已完成："):
    now=round((time + 1) * 100 / times,2)
    print('\r' + prompt + str(now), end='%', flush=True)

if __name__=='__main__':
    threeD()