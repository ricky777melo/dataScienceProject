import util.file as file

'''
实现数据类,功能如下：
将test_data.json文件夹中的相关数据提取出来
（可先用较小的sample.json练习）
可以自己增加方法
'''

class RawData:
    def __init__(self):
        self.__caseList=[]

    def __init__(self,src):
        #todo:读取处理好的数据
        data=file.read(src)
        self.__caseList =[]
        for item in data:
            self.__caseList.append(RawData.caseItem())

    def dispose(self,jsonPath):
        #todo：读取test_data.json并进行相关操作，实例化Item对象并append到dataList中
        pass
    def save(self,filePath):
        #todo:把dataList数据保存为.csv文件在data/dataBase目录下
        #文件中每一行为一个item
        pass


    class caseItem:
        def __init__(self,caseId,finalScore,caseContent,upLoadFre,upLoadTime,aveCodeLines):
            self.__caseId=caseId

            self.__caseContent=caseContent#题目内容，string类型，建议用json中的地址下下来保存，详情可看“《数据科学与基础》大作业补充说明.pdf”

            #一定要剔除掉一些数据，比如某个人没有写这道题，计算平均代码行数的时候就不考虑这个人
            self.__aveFinalScore=finalScore#学生平均得分
            self.__aveFre=upLoadFre#学生平均最大上传次数
            self.__time=upLoadTime#学生平均用时（用最后一次上传时间戳减去第一次上传时间戳来估计）
            self.__aveCodeLines=aveCodeLines#学生平均代码行数，每个学生的代码行数用最后一次提交的代码行数代替？
        def getCaseId(self):
            return self.__caseId
        def getFinalSc(self):
            return self.__aveFinalScore
        def getCaseContent(self):
            return self.__caseContent
        def getUpLoadFre(self):
            return self.__aveFre
        def getTime(self):
            return self.__time