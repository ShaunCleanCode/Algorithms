#  Dynamic Programming :Fibonacci Sequence
d= [0]* 100

def fibonnacci(x):
    if x ==1 or x==2:
        return 1
    
    if d[x]!=0:
        return d[x]
    
    d[x] =fibonnacci(x-1)+fibonnacci(x-2)
    return d[x]


print(fibonnacci(99))


    
    