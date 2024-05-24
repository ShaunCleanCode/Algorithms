def solution(a):
    n=len(a)
    for i in range(n):
        for j in range(i,n):
            a[i][j],a[j][i]=a[j][i],a[i][j]
            
    for i in range(n):
        for j in range(n//2):
            a[i][j],a[i][n-1-j]=a[i][n-1-j],a[i][j]
             
    
            
    return a
            

