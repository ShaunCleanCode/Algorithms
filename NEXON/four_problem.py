import math
import heapq

def min_cost_to_make_equal(nums):
    # 최소 힙 생성
    min_heap = []
    # 모든 숫자에 대한 비용을 힙에 추가
    for num in nums:
        heapq.heappush(min_heap, num)
    
    total_cost = 0
    # 힙이 한 개의 숫자만 남을 때까지 반복
    while len(min_heap) > 1:
        # 가장 작은 두 숫자를 힙에서 가져옴
        first = heapq.heappop(min_heap)
        second = heapq.heappop(min_heap)
        # 두 숫자를 같은 값으로 만드는 비용 계산
        if first == second:
            # 이미 같은 경우 비용이 들지 않음
            merged_num = first
        else:
            # 두 숫자 중 작은 것을 2배로 증가시키기
            merged_num = first * 2
            total_cost += 1
        # 계산된 새 숫자를 다시 힙에 추가
        heapq.heappush(min_heap, merged_num)
    
    # 최소 비용 반환
    return total_cost

# 예제 사용
nums = [4, 2, 8, 32, 128]
# 최소 비용 계산
print(min_cost_to_make_equal(nums))  # 결과는 최소 비용이어야 함

# 주어진 배열
nums = [10,
1,
2,
3,
4,
5,
6,
7,
8,
9,
10
]
# 최소 비용 계산
print(min_cost_to_make_equal(nums))  # 출력값은 최소 비용
