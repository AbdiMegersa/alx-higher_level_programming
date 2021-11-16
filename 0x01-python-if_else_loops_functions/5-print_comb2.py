#!/usr/bin/python3
for number in range(100):
    if number <= 9:
        print("{:d}{:d}".format(0, number), end=", ")
    elif number >= 10 and number < 99:
        print("{}".format(number), end=", ")
    else:
        print("{}".format(number))

