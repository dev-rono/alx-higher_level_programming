#!/usr/bin/python3

for num in range(100):
    print("0{}".format(num) if num < 10 else "{}".format(
        num), end=", " if num != 99 else "")
print()
