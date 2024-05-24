from collections import Counter

def commonCharacterCount(s1, s2):
    # 두 문자열의 문자 빈도수를 카운트
    counter1 = Counter(s1)
    counter2 = Counter(s2)
    
    # 공통 문자 수를 계산
    common_count = 0
    
    # counter1의 각 문자에 대해 반복
    for char in counter1:
        if char in counter2:
            # 두 카운터 모두에 존재하는 문자의 수를 찾아서 더 작은 값 더하기
            common_count += min(counter1[char], counter2[char])
    
    return common_count

# 예제 사용
s1 = "aabcc"
s2 = "adcaa"
print(commonCharacterCount(s1, s2))  # 결과는 3
