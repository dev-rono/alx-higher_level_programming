#!/usr/bin/python3

def uppercase(str):
    for char in str:
        char = ord(char)
        if 97 <= char <= 122:
            char -= 32
        char = chr(char)
        print("{}".format(char), end="")
    print()
