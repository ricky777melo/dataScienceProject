'''
实现数据类,功能如下：
将test_data.json文件夹中的相关数据提取出来
（可先用较小的sample.json练习）
'''
class RawData:
    def __init__(self):
        self.dataList=[]
    class line:
        def __init__(self):
            self.user_id
            self.case_id
            self.final_score
            self.case_type
            self.case_content#题目内容属性，string类型，建议用json中的地址下下来保存，详情可看“《数据科学与基础》大作业补充说明.pdf”
            self.upLoad_fre#最大上传次数
            self.upLoad_timestamp=[]#每次上传的时间戳，列表类型，长度为最大上传次数


