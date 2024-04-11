# 입력값 N 




    

def f_x(x):
    cp_str=''
    square_x= str(int(x)**2)
    k=int(len(x))
    last_index=len(square_x)-1
    for i in range(last_index-k+1,last_index+1):
        cp_str+= square_x[i]
        
    if(cp_str==x):
        return 1
    else:
        return 0
    

# 주어진 n에 대해서 x<n, f(x)=1을 만족하는 가장 큰 정수를 찾는 함수
def find_largest_fx(n):
    for x in range(int(n)-1, 0, -1):  # n-1부터 1까지 역순으로 탐색
        if f_x(str(x)) == 1:
            return x
    return None  # 조건을 만족하는 x가 없는 경우
    

            
while True:
    n=input("Enter n: ")
    print(find_largest_fx(n))
