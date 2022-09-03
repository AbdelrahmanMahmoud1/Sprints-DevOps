


def MyFunc(list):
    mean = 0
    count = 0
    sum = 0
    max = 0
    for i in list:
        if (isinstance(i,int)):
            if (i % 2 == 0):
                sum+=i
                count+=1
        elif (isinstance(i,float)):
            if (i > max):
                max = i

    mean = sum/count
    return (max, mean)




