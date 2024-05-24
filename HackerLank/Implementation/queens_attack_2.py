#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#
    
def queensAttack(n, k, r_q, c_q, obstacles):
    
    attacks_count=0
    obstacles_set= set(obstacles)
    # Define directions: right, left, up, down, and the four diagonal directions
    directions = [
        (0, 1), (0, -1), (1, 0), (-1, 0),
        (1, 1), (1, -1), (-1, 1), (-1, -1)
    ]
    for dr, dc in directions:
        current_rows, current_cols= r_q,c_q
        
        while True:
            current_rows+=dr
            current_cols+=dc
            
            # Check if there is an obstacle
            if 1<=current_rows<= n and 1<= current_cols <=n:
                if (current_rows, current_cols) in obstacles_set:
                    break
                attacks_count+=1
            # If out of bounds, stop in this direction
            else:
                break
    

    return attacks_count
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    r_q = int(second_multiple_input[0])

    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(tuple(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
