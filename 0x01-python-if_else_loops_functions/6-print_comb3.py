#!/usr/bin/python3
for t in range(10):
    for w in range(t, 10):
        if t < w:
            print("{:d},{:d}".format(t, w),
                    end="\n" if t == 8 and w == 9 else ", ")
