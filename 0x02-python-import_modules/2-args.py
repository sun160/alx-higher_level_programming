#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    arg = sys.argv
    count = len(arg) - 1

    if count > 1:
        print("{} arguments:".format(count))
        for i in range(count):
            print("{}: {}".format(i + 1, arg[i + 1]))

    elif count == 0:
        print("{} arguments.".format(count))

    else:
        print("{} argument:".format(count))
        print("{}: {}".format(count, arg[1]))
