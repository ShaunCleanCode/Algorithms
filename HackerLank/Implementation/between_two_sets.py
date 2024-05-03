#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#
import math

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def lcm(x, y):
    return x * y // gcd(x, y)

def getTotalX(a, b):
    # 첫 번째 배열의 LCM 계산
    l = a[0]
    for num in a[1:]:
        l = lcm(l, num)

    # 두 번째 배열의 GCD 계산
    g = b[0]
    for num in b[1:]:
        g = gcd(g, num)

    # LCM이 GCD의 약수가 아니라면 만족하는 수가 없음
    if g % l != 0:
        return 0

    # LCM부터 GCD까지 LCM의 배수 세기
    count = 0
    multiple = l
    while multiple <= g:
        if g % multiple == 0:
            count += 1
        multiple += l

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
