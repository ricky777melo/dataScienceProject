def floatArray(data,dim=2):
    answer=[]
    for i in range(data.__len__()):
        if dim==2:
            answer.append([float(x) for x in data[i]])
        if dim==1:
            answer.append(float(data[i]))
    return answer
def intArray(data,dim=2):
    answer=[]
    for i in range(data.__len__()):
        if dim == 2:
            answer.append([int(x) for x in data[i]])
        if dim == 1:
            answer.append(int(data[i]))
    return answer