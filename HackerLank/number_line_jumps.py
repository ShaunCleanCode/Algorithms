#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    # Write your code here
    x1_position=0
    x2_position=0
    # 처음부터 따라 잡을 수 없음
    if (x1 <x2 and v1<= v2) or (x1>x2 and v1>=v2):
        return "NO"
    # 한번 앞서면 따라 잡을 수 없음
    elif x1<x2 and v1> v2:
        x1_position=x1
        x2_position=x2
        while x1_position <=x2_position:
            x1_position+=v1
            x2_position+=v2
            if x1_position==x2_position:
                return "YES"
        return "NO"
    # 한번 앞서면 따라 잡을 수 없음
    elif x1>x2 and v1<v2:
        x1_position=x1
        x2_position=x2
        while x1_position >=x2_position:
            x1_position+=v1
            x2_position+=v2
            if x1_position==x2_position:
                return "YES"
        return "NO"
    

    return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
