def initialize_dp(n, m, cache_array):
    """
    2차원 배열(dp)을 초기화하는 함수
    :param n: 세로 크기
    :param m: 가로 크기
    :param cache_array: 입력된 1차원 배열
    :return: 초기화된 2차원 배열(dp)
    """
    dp = [[0 for _ in range(m)] for _ in range(n)]
    for j in range(n):
        for k in range(m):
            dp[j][k] = cache_array[j*m + k]
    return dp

def calculate_max_gold(dp, n, m):
    """
    각 위치에서 얻을 수 있는 금의 최대 양을 계산하는 함수
    :param dp: 초기화된 2차원 배열(dp)
    :param n: 세로 크기
    :param m: 가로 크기
    """
    for j in range(1, m):
        for i in range(n):
            # 왼쪽 위, 왼쪽, 왼쪽 아래에서 오는 경우 계산
            left_up = dp[i-1][j-1] if i != 0 else 0
            left = dp[i][j-1]
            left_down = dp[i+1][j-1] if i != n-1 else 0

            dp[i][j] += max(left, left_down, left_up)

def find_max_gold(dp, n, m):
    """
    dp 배열에서 금의 최대 양을 찾는 함수
    :param dp: 계산된 2차원 배열(dp)
    :param n: 세로 크기
    :param m: 가로 크기
    :return: 금의 최대 양
    """
    result = 0
    for i in range(n):
        result = max(result, dp[i][m-1])
    return result

# 메인 코드
for tc in range(int(input())):
    n, m = map(int, input().split())
    cache_array = list(map(int, input().split()))
    
    # 2차원 배열 초기화
    dp = initialize_dp(n, m, cache_array)
    
    # 금의 최대 양 계산
    calculate_max_gold(dp, n, m)
    
    # 결과 출력
    print(find_max_gold(dp, n, m))
