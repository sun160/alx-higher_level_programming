#!/usr/bin/python3
for w in range(25, -1, -1):
    m = w + ord('A')
    if w % 2 == 1:
        m += 32
    print("{}".format(m), end=" ")
