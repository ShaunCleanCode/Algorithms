#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'legoBlocks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def legoBlocks(n, m):
    
    MOD= (10**9)+7
    array_sm =[0] *1002
    array_sm[0]=0
    array_sm[1]=1
    array_sm[2]=2
    array_sm[3]=4
    array_sm[4]=8
    if m>=5:
        for i in range(5, m+1):
            array_sm[i] = (array_sm[i-1] + array_sm[i-2] + array_sm[i-3] + array_sm[i-4]) % MOD

    
    # Calculate total configurations for all rows
    all_case = [1] * (m+1)
    for i in range(1, m+1):
        all_case[i] = (array_sm[i]**n)% MOD
    
    # Calculate the number of configurations with vertical breaks
    solid_case = [1] * (m+1)
    for width in range(1, m+1):
        unsolid_case = 0
        for break_point in range(1, width):
            unsolid_case += (solid_case[break_point] * all_case[width - break_point]) % MOD
            unsolid_case %= MOD
        solid_case[width] = (all_case[width] - unsolid_case + MOD) % MOD
    
    # Return the number of valid configurations for the entire wall of size n x m
    return solid_case[m]

    
if __name__ == '__main__':


    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = legoBlocks(n, m)

        print((str(result) + '\n'))


