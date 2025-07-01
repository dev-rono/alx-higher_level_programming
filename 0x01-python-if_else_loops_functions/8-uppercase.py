#!/usr/bin/env python3

def uppercase(str):
    new_str = ""
    for char in str:
        char = ord(char)
        if (char > 96):
            char -= 32
        new_str += chr(char)
    print(new_str)
print()
