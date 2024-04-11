# Reads the target number from user input
n = int(input())


d = [0] * 100
d[1] = 0  # Base case: 0 

def dynamic_programming(n):
   
    for i in range(2, n + 1):

        d[i] = d[i - 1] + 1

        if i % 5 == 0:
            d[i] = min(d[i], d[i // 5] + 1)
        

        elif i % 3 == 0:
            d[i] = min(d[i], d[i // 3] + 1)
        

        elif i % 2 == 0:
            d[i] = min(d[i], d[i // 2] + 1)
        
    print(d[n])
    

dynamic_programming(n)
