# 주어진 문자열 s가 팰린드롬인지 확인하는 함수입니다.
def is_palindrome(s):
    return s == s[::-1]  # 문자열을 뒤집어서 원래 문자열과 비교합니다.

# 주어진 문자열에서 하나의 문자를 제거하여 팰린드롬을 만들 수 있는지 확인하고,
# 해당 문자의 위치를 반환하는 함수입니다.
def palindrome_index(s):
    if is_palindrome(s):
        return -1  # 만약 이미 팰린드롬이면 -1을 반환합니다.

    # 문자열의 양 끝에서 시작하여 가운데로 진행하면서 검사합니다.
    left, right = 0, len(s) - 1
    while left < right:
        # 왼쪽과 오른쪽 문자가 다를 경우
        if s[left] != s[right]:
            # 오른쪽 문자를 제거했을 때 나머지 문자열이 팰린드롬이 되는지 확인합니다.
            if is_palindrome(s[left:right]):
                return right  # 팰린드롬이 되면, 제거된 오른쪽 문자의 인덱스를 반환합니다.
            # 왼쪽 문자를 제거했을 때 나머지 문자열이 팰린드롬이 되는지 확인합니다.
            elif is_palindrome(s[left + 1:right + 1]):
                return left  # 팰린드롬이 되면, 제거된 왼쪽 문자의 인덱스를 반환합니다.
            # 만약 양쪽 문자를 제거해도 팰린드롬이 되지 않는다면,
            # 더 이상의 검사는 무의미하므로 반복문을 종료합니다.
            break
        # 왼쪽과 오른쪽 인덱스를 중앙으로 옮겨가며 계속 검사합니다.
        left, right = left + 1, right - 1

    # 모든 검사를 마쳤으나 팰린드롬을 만들 수 없으면 -1을 반환합니다.
    return -1

# 함수 실행 및 테스트
print(palindrome_index("aaab"))  # 3 반환
print(palindrome_index("baa"))   # 0 반환
print(palindrome_index("aaa"))   # -1 반환 (이미 팰린드롬이므로)
