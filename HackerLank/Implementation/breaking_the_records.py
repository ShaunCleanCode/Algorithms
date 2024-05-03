#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#
def breakingRecords(scores):
    min_value = scores[0]
    max_value = scores[0]
    min_breaks = 0
    max_breaks = 0
    
    for score in scores[1:]:  
        if score < min_value:
            min_value = score
            min_breaks += 1
        if score > max_value:
            max_value = score
            max_breaks += 1
    
    return [max_breaks, min_breaks]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    scores = list(map(int, input().rstrip().split()))
    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
