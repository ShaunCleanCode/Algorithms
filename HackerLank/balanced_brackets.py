
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def isBalanced(s):
  # 괄호의 쌍을 정의
    bracket_pair = {')': '(', '}': '{', ']': '['}
    stack = []  # 열린 괄호를 저장할 스택

    for char in s:
        # 닫힌 괄호인 경우
        if char in bracket_pair:
            # 스택이 비어있거나, 스택의 마지막 원소가 해당 닫힌 괄호와 쌍을 이루지 않으면 "NO" 반환
            if not stack or stack[-1] != bracket_pair[char]:
                return "NO"
            stack.pop()  # 스택에서 마지막 열린 괄호를 제거
        else:
            # 열린 괄호인 경우 스택에 추가
            stack.append(char)

    # 스택이 비어있으면 모든 괄호가 쌍을 이루어 "YES", 그렇지 않으면 "NO" 반환
    return "YES" if not stack else "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
