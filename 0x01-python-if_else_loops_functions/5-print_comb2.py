#!/usr/bin/python3

for num in range(100):
    if (len(str(num)) == 1):
        print("0{}, ".format(num), end = "")
    else:
        print("{}, ".format(num), end="")
