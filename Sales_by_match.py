#!/bin/python3

import math
import os
import random
import re
import sys


def sockMerchant(n, ar):
    se = set(ar)
    fn_cnt = 0
    for i in se:
        cnt = ar.count(i)
        fn_cnt += cnt//2
    return(int(fn_cnt))


if __name__ == '__main__':
    print("Enter the length of the array:")
    n = int(input())
    print("Enter the array")
    ar = list(map(int, input().rstrip().split()))
    result = sockMerchant(n, ar)
    print("Number of matching pairs:")
    print(str(result) + '\n')
