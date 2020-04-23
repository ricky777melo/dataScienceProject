import os
def read(thePath,dim=2,gap=",",ifFloat=False):
    '''

    :param thePath of the csvFile
    :return:
    '''
    if dim==2:
        with open(thePath, 'r', encoding='utf-8') as f:
            data = f.read().split('\n')
        length=data.__len__()
        for i in range(length):
            data[i]=data[i].split(gap)
            if ifFloat:
                for j in range(data[i].__len__()):
                    try:
                        data[i][j]=float(data[i][j])
                    except:
                        data[i][j]=i
    if dim==1:
        with open(thePath, 'r', encoding='utf-8') as f:
            data = f.read().split(gap)
            if ifFloat:
                data=[float(x) for x in data]
    return data

def write(thePath,data,dim=2,gap=','):
    '''

    :param thePath:
    :param data:二维数组
    :return:
    '''
    if dim==2:
        with open(thePath, 'w', encoding='utf-8') as f:
            length=data.__len__()
            for i in range(length):
                line=[str(x) for x in data[i]]
                f.writelines(gap.join(line))
                if i!=length-1:
                    f.writelines("\n")
    if dim==1:
        with open(thePath, 'w', encoding='utf-8') as f:
            data=[str(x) for x in data]
            f.writelines(gap.join(data))
    return True

def getRootPath():
    cur_path = os.path.abspath(os.path.dirname(__file__))
    root_path = cur_path[:cur_path.find("dataScienceProject\\") + len("dataScienceProject\\")]
    return root_path