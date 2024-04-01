from bisect import bisect_left,bisect_right

n,x =map(int,input().split())

sequence =list(map(int,input().split()))

def count_num(sequence,x):
    
    return bisect_right(sequence,x)-bisect_left(sequence,x)

print(count_num(sequence,x))