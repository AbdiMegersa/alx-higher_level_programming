#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    newList = []
    for x in my_list:
        if x not in newList:
            newList.append(x)
    for i in newList:
        sum += i
    return sum
