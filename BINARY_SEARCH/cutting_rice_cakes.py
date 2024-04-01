# 떡의 개수와 요구하는 떡의 길이를 입력받음
n, m = map(int, input().split())

# 각 떡의 개별 높이를 입력받음
ddduck_height = list(map(int, input().split()))

# 이진 탐색을 위한 시작점과 끝점 설정
start = 0
end = max(ddduck_height)

# 이진 탐색을 통해 찾은 떡 절단기의 높이를 저장할 변수
result = 0

# 이진 탐색 시작
while (start <= end):
    total = 0  # 잘린 떡의 총 길이를 저장할 변수
    mid = (start + end) // 2  # 중간점 계산
    
    # 각 떡을 중간점 높이로 자른 후의 길이를 계산
    for x in ddduck_height:
        if x > mid:
            total += x - mid
    
    # 잘린 떡의 총 길이가 요구 길이보다 작으면 더 많이 자르기 (끝점을 줄임)
    if total < m:
        end = mid - 1
    # 잘린 떡의 총 길이가 요구 길이보다 크거나 같으면 덜 자르기 (시작점을 늘림)
    else:
        result = mid  # 최대한 덜 자른 것이 정답이므로 여기에서 result를 갱신
        start = mid + 1

# 결과 출력
print(result)
