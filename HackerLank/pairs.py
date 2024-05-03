#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'pairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def pairs(k, arr):

    count = 0
    # 배열 arr의 모든 원소가 유니크하다고 했으므로, 빠른 검색을 위해 set을 사용합니다. o (1)
    set_arr = set(arr)
    # set_arr에 있는 각 x에 대해, k만큼 차이나는 값이 set_arr에 있는지 확인합니다.
    for x in set_arr:
        # x와 정확히 k만큼 차이나는 값(-(k - x))이 set에 있는지 확인합니다.
        if -(k - x) in set_arr:
            # 해당 값이 있다면 count를 1 증가시킵니다.
            count += 1
    
    # 최종적으로 찾은 쌍의 수를 반환합니다.
    return count

            
    
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
