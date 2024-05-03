def superDigit(p):
    # 'p'의 길이가 1이면, 'p'를 정수로 변환하여 반환합니다.
    if len(p) == 1:
        return int(p)
    else:
        # 'p'의 각 자릿수의 합을 계산합니다.
        sum_of_digits = sum(int(digit) for digit in p)
        # 계산된 합을 문자열로 변환하여 superDigit 함수에 재귀적으로 호출합니다.
        return superDigit(str(sum_of_digits))
            

def superDigitCall(n, k):
    # 'n'의 각 자릿수의 합을 계산합니다.
    initial_sum = sum(int(digit) for digit in n)
    # 계산된 합에 'k'를 곱합니다. 이는 'n'을 'k'번 반복한 것과 같은 효과를 내는데, 
    # 실제로 문자열을 만들지 않고 합산한 값에 'k'를 곱하는 것으로 메모리를 절약할 수 있습니다.
    combined_sum = initial_sum * k
    # 최종적으로 계산된 합의 슈퍼 디지트를 구하기 위해 superDigit 함수를 호출합니다.
    return superDigit(str(combined_sum))
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigitCall(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
