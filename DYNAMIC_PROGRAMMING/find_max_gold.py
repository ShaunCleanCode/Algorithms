
for tc in range(int(input())):
    # 세로의 크기 n , 가로의 크기 m
    n,m=map(int,input().split())
    cache_array =list(map(int,input().split()))
    print(cache_array)
     # 2차원 배열 초기화
    dp = [[0 for _ in range(m)] for _ in range(n)]
    for j in range(n):
        for k in range(m):

            dp[j][k] = cache_array[j*m + k]

    print(dp)



for j in range(1,m):
    for i in range(n):
        # 왼쪽 위에서 오는 경우 
        if i ==0:
            left_up=0
        else:
            left_up=dp[i-1][j-1]
        # 왼쪽 아래에서 오는 경우
        if i==n-1:
            left_down=0
        else:
            left_down =dp[i+1][j-1]
        left =dp[i][j-1]
        
        dp[i][j]=dp[i][j]+max(left,left_down,left_up)
        
result=0
        
for i in range(n):
    result =max(result ,dp[i][m-1])
print(result)    

