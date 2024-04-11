# 총 병사의 수 입력 받기
n = int(input())

# 각 병사의 전투력 입력 받기
array = list(map(int, input().split()))

# 전투력을 기준으로 병사를 내림차순 배치하기 위해 배열을 뒤집는다.
array.reverse()

# DP 테이블 초기화: 각 병사를 마지막으로 하는 가장 긴 증가하는 부분 수열의 길이
dp = [1] * n

# 가장 긴 증가하는 부분 수열(LIS) 알고리즘 적용
for i in range(1, n):
    for j in range(0, i):
        # 현재 병사의 전투력이 이전 병사의 전투력보다 높은 경우, 부분 수열을 연장할 수 있다.
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j] + 1)

# 열외해야 하는 병사의 최소 수를 계산한다.
# 전체 병사 수에서 가장 긴 증가하는 부분 수열의 길이를 뺀 값이 열외해야 할 병사의 수다.
print(n - max(dp))
