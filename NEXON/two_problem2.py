from collections import Counter

def count_mex(arr, l, r):
    mex_counts = Counter()
    
    # 모든 숫자를 추적하며 각 숫자의 빈도수를 센다.
    number_freq = Counter(arr)
    
    # MEX 계산을 위해 필요한 숫자의 집합을 만든다.
    needed_numbers = set(range(r + 1))  # MEX는 최대 r이 될 수 있다.

    # 수열을 순회하며 MEX를 계산한다.
    for end in range(len(arr) + 1):
        for start in range(end + 1):
            current_numbers = set(arr[start:end])
            # MEX는 needed_numbers 중 current_numbers에 없는 가장 작은 수이다.
            mex = min(needed_numbers - current_numbers)
            if l <= mex <= r:
                mex_counts[mex] += 1

    # MEX가 l과 r 사이에 있는 부분수열의 총 개수를 반환한다.
    return sum(mex_counts[mex] for mex in range(l, r + 1))

# 입력 예시
arr = [0, 2, 4, 1, 0, 2, 3]
l = 0
r = 2


# 함수 호출 및 결과 출력
print(count_mex(arr, l, r))  # 결과는 부분수열의 MEX 값이 [L, R] 범위 안에 있는 경우의 수
