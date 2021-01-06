#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#


def countingValleys(steps, path):
    # Write your code here
    lvl = 0
    cnt = 0
    for i in range(steps):
        if path[i] == 'U':
            lvl += 1
            if lvl == 0:
                cnt += 1
        else:
            lvl -= 1
    return cnt


if __name__ == '__main__':
    print("ENter the number of steps")
    steps = int(input().strip())
    print("ENter the path")
    path = input()
    result = countingValleys(steps, path)
    print(str(result) + '\n')
