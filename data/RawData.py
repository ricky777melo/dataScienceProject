import util.file as file

'''
实现数据类,功能如下：
将test_data.json文件夹中的相关数据提取出来
（可先用较小的sample.json练习）
可以自己增加方法
'''


class RawData:
    def __init__(self):
        self.dataList=[]

    def __init__(self,src):
        #todo:读取处理好的数据
        data=file.read(src)
        self.dataList =[]
        for item in data:
            self.dataList.append(RawData.Item())

    def dispose(self,jsonPath):
        #todo：读取test_data.json并进行相关操作，实例化Item对象并append到dataList中
        pass
    def save(self,filePath):
        #todo:把dataList数据保存为.csv文件在data/dataBase目录下
        #文件中每一行为一个item
        pass



    class Item:
        def __init__(self):
            self.user_id
            self.case_id
            self.final_score
            self.case_type
            self.case_content#题目内容属性，string类型，建议用json中的地址下下来保存，详情可看“《数据科学与基础》大作业补充说明.pdf”
            self.upLoad_fre#最大上传次数
            self.upLoad_timestamp=[]#每次上传的时间戳，列表类型，长度为最大上传次数

