#!/usr/bin/python3

def uppercase(str):
    new_str = ""
    for char in str:
        char = ord(char)
        print("char 0: ", char)
        if (char > 96):
            print("char 1: ", char)
            char -= 32
            print("char 2: ", char)
        new_str += chr(char)
    print("{}".format(new_str))
uppercase("alx")
