#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # my_list is the initial list
    # search is the element to replace in the list
    # replace is the new element
    newList = my_list.copy()
   
    for i in newList:
        if i == search:
            index = newList.index(i)
            newList[index] = replace
    return newList
