#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    num_args = len(argv) - 1

    if num_args == 0:
        print("{} arguments.".format(0))

    else:
        plural = "arguments:" if num_args > 2 else "argument:"
        print("{} {}".format(num_args, plural))
        for num in range(1, num_args + 1):
            print("{}: {}".format(num, argv[num]))
