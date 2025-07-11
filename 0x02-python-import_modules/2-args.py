#!/usr/bin/python3

from sys import argv

num_args = len(argv) - 1

if num_args - 1 >= 3:
    print("{} arguments:".format(num_args))
else:
    print("{} argument:".format(num_args))

for num in range(1, num_args + 1):
    print("{}: {}".format(num, argv[num]))
