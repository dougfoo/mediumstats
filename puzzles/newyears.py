#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.

#                            1 2 5 3 7 8 6 4  <- flip 1 slot
#                            1 2 3 5 7 8 6 4  <- flip 1 slot
#                            1 2 3 5 7 6 8 4  <- flip 1 slot
#                            1 2 3 5 6 7 8 4
#                            1 2 3 5 6 7 4 8
#                            1 2 3 5 6 4 7 8
#                            1 2 3 5 4 6 7 8
#                            1 2 3 4 5 6 7 8
# left to right, mark where there is non-seq
# stop when left > right and flip
# restart at last non-seq
#                          1  2  5  3  7  8  6  4  <- flip 1 slot
def minimumBribes(q):
    for i, a in enumerate(q):
        if (a - (i + 1) > 2):
            print('Too chaotic')
            return -1

    prev = 0
    lastOrdered = 0
    bribes = 0
    dirty = True

    while (dirty):
        dirty = False
        prev = 0
        for i,a in enumerate(q):
            if (prev != 0):
                if (prev+1 == a):
                    lastOrdered = i   # defect if you have 1,2,5,3,4
                if (a < prev):
                    q[i] = prev
                    q[i-1] = a
                    bribes += 1
                    dirty = True
                    continue
            prev = a
    print(bribes)
    return bribes


def minimumBribes2(q):
    print(q)
    # max 2 off original
    # count how many each are off original
    # only bribe/swap folks to left (front)
    # 2 1 5 3 4 -> 5 is 2 off, 2 is 1 off
    #  start left to right?   swap any out of order
    steps = 0
    for i,a in enumerate(q):
#        print (f'i {i} a {a}')
        if (i+1 > a):
            pass
        elif(a - (i+1) > 2):
            print('Too chaotic')
            return -1
        else:
            steps += a - (i+1)
    print(steps)
    return steps

if __name__ == '__main__':
    t = 2
    input = ["5 1 2 3 7 8 6 4", "1 2 5 3 7 8 6 4"]

    for t_itr in range(len(input)):
        q = list(map(int, input.pop().split(' ')))
        minimumBribes(q)
