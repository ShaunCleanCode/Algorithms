#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
# O (nlogn)

def nonDivisibleSubset(k, s):
    # Write your code here

    longest_subset=0
    #1.
    for i in range(len(s)):
        s[i]= s[i]% k
    #2.
    count=[0] * (k)
    for i in range(len(s)):
        count[s[i]] +=1
    #3.  
    dic={i:count[i] for i in range(len(count))}
    print(dic)
    #4.
    if dic[0]!=0:
        longest_subset+=1
    #5.
    for i in range(1, (k//2)+1):
        if k%2==0 and i ==k//2 and dic[i]!=0:
            longest_subset+=1
        else:
            longest_subset+=max(dic[i], dic[k-i])
        
    
    return longest_subset

        
        
        
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
