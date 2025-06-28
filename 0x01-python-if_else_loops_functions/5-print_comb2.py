#!/usr/bin/python3

for num in range(100):
    if (len(str(num)) == 1):
        print("0{}".format(num), end = ", " if num != 99 else " ")
    else:
        print("{}".format(num), end=", " if num != 99 else " ")
