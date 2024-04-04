# bisect 모듈에서 bisect_left와 bisect_right 함수를 가져옵니다.
from bisect import bisect_left, bisect_right

# n은 수열의 크기, x는 찾고자 하는 값
n, x = map(int, input().split())

# 수열을 입력받아 리스트로 만듭니다.
sequence = list(map(int, input().split()))

# 특정 범위에 속하는 데이터의 개수를 계산하는 함수
def count_by_range(sequence, x):
    # x 값이 시작되는 인덱스
    left_index = bisect_left(sequence, x)
    # x 값이 끝나는 인덱스
    right_index = bisect_right(sequence, x)
    # x 값이 수열에 존재하지 않는 경우
    if (left_index == right_index):
        return -1
    # x 값이 수열에 존재하는 경우, 개수를 반환
    return right_index - left_index

# 함수를 호출하여 결과를 출력합니다.
print(count_by_range(sequence, x))
