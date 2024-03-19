import time



def minus_one(n):
    return n-1

def divide_k(n,k):
    return n//k

def count_one_and_two(n,k):
    count =0
    while n != 1:
        if (n%k==0):
            n=divide_k(n,k)
            count +=1
        else:
            n=minus_one(n)
            count+=1
    return count

def main():
   
    
    #N,K 를 공백 기준으로 구분해서 입력받기
    n,k = map(int(input.split()))
    
    result =count_one_and_two(n,k)
    print(result)
    


# 시작 시간 측정
start_time = time.time()
main()
# 종료 시간 측정
end_time = time.time()

# 수행 시간 출력
print(f"수행 시간: {end_time - start_time}초")



    
            
        
