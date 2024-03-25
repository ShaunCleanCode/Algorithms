# 1. 두개의 배열 A, B 

# 2. 두 배열은 N개의 원소로 구성 , 모두 자연수 

# 3. K 번까지 바꿔치기 가능

# 4. A 배열의 합이 최대가 되도록 해야함.

# 5. A 배열에서 가장 작은 값들 부터 B 배열에서 가장 큰 값들을 비교함.

# 6.  A배열 가장 작은 값 < B 배열 큰 값 이면 스왑 하고 카운트
n,k =map(int,input().split()) # N 과 K 입력받기
a= list(map(int,input().split()))
b= list(map(int,input().split()))
count =0

def sort(a,b):
    a.sort()   
    b.sort(reverse =True)
    
def swap(a,b,k):  
    
    for i in range(k):
        
        if a[i] < b[i]:
            a[i],b[i] =b[i],a[i]
       
        break
        
sort(a,b)
swap(a,b)
print(sum(a))