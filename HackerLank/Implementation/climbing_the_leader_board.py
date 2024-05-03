#!/bin/python3

import math
import os
import random
import re
import sys
import bisect

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):

    unique_ranked = sorted(set(ranked), reverse=True)
    
    result = []
    len_ranked = len(unique_ranked)
   
    for score in player:
       
        if score >= unique_ranked[0]:
            result.append(1)  
        elif score < unique_ranked[-1]:
            result.append(len_ranked + 1)  
        else:
            low, high = 0, len_ranked
            while low < high:
                mid = (low + high) // 2
                if unique_ranked[mid] > score:
                    low = mid + 1
                else:
                    high = mid
            result.append(low + 1)  

    return result

    
    
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
