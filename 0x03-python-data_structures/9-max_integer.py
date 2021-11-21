#!/usr/bin/python3
def max_integer(my_list=[]):
    largest = 0
    if my_list == []:
        return None
    else:
        for i in range(len(my_list)):
            if (largest < int(my_list[i])):
                largest = my_list[i]
        return largest
