#!/usr/bin/python3

def uppercase(str):
    new_str = ""
    for char in str:
        char = ord(char)
        if 97 <= char <= 122:
            char -= 32
        new_str += chr(char)
    print("{}".format(new_str))
print()
