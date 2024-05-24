#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'almostSorted' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'almostSorted' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#
def almostSorted(arr):
    sorted_arr = sorted(arr)
    

    if arr == sorted_arr:
        print('yes')
        return
    
    index_list = []
    
    for i in range(len(sorted_arr)):
        if sorted_arr[i] != arr[i]:
            index_list.append(i+1)
    

    if not index_list:
        print('yes')
        return
    
    if len(index_list) == 2:
        print('yes')
        print('swap ' + str(index_list[0]) + ' ' + str(index_list[1]))
    else:
        sub_list = arr[index_list[0]-1: index_list[-1]]
        if sorted(sub_list, reverse=True) == arr[index_list[0]-1: index_list[-1]]:
            print('yes')
            print('reverse ' + str(index_list[0]) + ' ' + str(index_list[-1]))
        else:
            print('no')


    
            

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    almostSorted(arr)

    
            

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    almostSorted(arr)
