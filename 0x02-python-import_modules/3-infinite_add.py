#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0
    arg = sys.argv

    for x in range(len(arg) - 1):
        sum += int(arg[x + 1])
    print(sum)
