# 총 병사의 수  N 
n =int(input())

# 인풋 병사 배열 
array=list(map(int,input().split()))

array.reverse()

# DP 초기화 
dp=[1]*n

# 가장 긴 증가하는 부분 수열을 찾는 알고리즘 LIS 진행

for i in range(1,n):
    for j in range(0,i):
        if array[j] < array[i]:
            dp[i] =max(dp[i],dp[j]+1)
            


print(n-max(dp))

