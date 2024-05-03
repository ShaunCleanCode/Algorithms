#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):
    # 주어진 그리드의 길이를 n에 저장합니다.
    n = len(grid)
    # 문자열의 길이를 string_length에 저장합니다. 모든 문자열은 같은 길이를 가집니다.
    string_length = len(grid[0])
    # 각 문자열을 알파벳 순으로 정렬합니다.
    for i in range(n):
        grid[i] = ''.join(sorted(grid[i]))
    # 각 열에 대해서 검사를 진행합니다.
    for i in range(string_length):
        # 현재 열의 모든 행을 검사합니다.
        for j in range(0, n-1):
            # 현재 위치의 문자가 다음 행의 같은 열 위치의 문자보다 사전 순으로 뒤에 오면,
            # 그리드는 요구 조건을 만족하지 않으므로 "NO"를 반환합니다.
            if ord(grid[j][i]) > ord(grid[j+1][i]):
                return "NO"
    # 모든 검사를 통과하면, 그리드는 요구 조건을 만족하므로 "YES"를 반환합니다.
    return "YES"
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()
