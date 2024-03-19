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
    # 시작 시간 측정
    start_time = time.time()
    result =count_one_and_two(1000000,2)
    print(result)
    # 종료 시간 측정
    end_time = time.time()

    # 수행 시간 출력
    print(f"수행 시간: {end_time - start_time}초")


    
main()



    
            
        
