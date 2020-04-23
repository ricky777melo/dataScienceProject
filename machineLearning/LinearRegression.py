import math
import util.IO as RI
class LinearRegression:
    def __init__(self,dataX,dataY,alpha,maxTimes):
        self.__theta=[]
        self.__dim=dataX[0].__len__()
        self.__sampleSize=dataX.__len__()
        self.__dataX=dataX
        self.__dataY=dataY
        self.__alpha=alpha
        self.__maxTimes=maxTimes
        self.__Jvalue=[]

    def costFunction(self):
        '''
        代价函数
        :param theta:
        :param data: float！！
        :return:
        '''
        answer = 0
        len = self.__sampleSize
        for i in range(len):
            hx = self.productTheta(self.__dataX[i])
            add = (hx-self.__dataY[i])**2
            answer += add
        answer /= 2*len
    def gradientDescent(self):
        self.__Jvalue.clear()
        for time in range(self.__maxTimes):
            thetaNext = self.__theta.copy()
            for j in range(self.__dim):
                sub = 0
                for ii in range(self.__sampleSize):
                    add = (self.productTheta(self.__dataX[ii])-self.__dataY[ii])*self.__dataX[ii][j]
                    sub += add
                sub=sub/self.__sampleSize
                sub = sub * self.__alpha
                thetaNext[j] = thetaNext[j] - sub
            self.__theta = thetaNext
            self.__Jvalue.append(self.costFunction())
            RI.progressBar(time,self.__maxTimes,"正在梯度下降")
    def productTheta(self,x):
        answer = 0
        for i in range(self.__dim):
            answer = x[i] * self.__theta[i]
        return answer

        