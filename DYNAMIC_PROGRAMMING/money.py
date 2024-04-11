# 입력 받기: n은 화폐 종류의 수, m은 만들고자 하는 금액
n, m = map(int, input().split())

# d 배열은 각 금액을 만들기 위한 최소 화폐 개수를 저장 (초기값은 무한대로 설정)
d = [10001] * (m + 1)
d[0] = 0 # 0원을 만드는 데는 0개의 화폐가 필요

# 화폐 단위를 저장할 리스트
array = []
for i in range(n):
    unit = int(input()) # 화폐 단위 입력 받기
    array.append(unit)
    
# 화폐 단위 배열을 사용하여 금액 m을 만들 수 있는 최소 화폐 개수 계산
def calculate_min_units(n, m, d, array):
    for i in range(n):
        for j in range(array[i], m + 1):
            if d[j - array[i]] != 10001: # (현재 금액 - 화폐 단위)를 만드는 방법이 존재하면
                d[j] = min(d[j], d[j - array[i]] + 1) # 최소 화폐 개수 갱신
    
    # 최종적으로 m원을 만들 수 있는 최소 화폐 개수 출력
    if d[m] == 10001: # 만들 수 없는 경우
        print(-1)
    else:
        print(d[m])

calculate_min_units(n, m, d, array)
