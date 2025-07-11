#!/usr/bin/python3

from sys import argv

num_args = len(argv) - 1
print("{}".format(num_args), end=" ")

if num_args - 1 >= 3:
    print("arguments:")
else:
    print("argument:")

for num in range(1, num_args + 1):
    print("{}: {}".format(num, argv[num]))
