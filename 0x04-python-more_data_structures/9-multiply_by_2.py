#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newDict = {}
    newValue = 0
    for x in a_dictionary:
        newValue = a_dictionary.get(x) * 2
        newDict.update({x: newValue})
