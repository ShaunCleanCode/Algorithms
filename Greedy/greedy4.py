
def move_left(x,y,n):
    if y==1:
        return x,y
    
    return x,y-1

def move_right(x,y,n):
    if y==n:
        return x,y
    
    return x,y+1

def move_up(x,y,n):
    if x==1:
        return x,y
    return  x -1,y

def move_down(x,y,n):
    if x==n:
        return x,y 
    return  x +1,y

operations ={
    'L':move_left,
    'R':move_right,
    'U':move_up,
    'D': move_down
    
}

def operate(operator,x,y,n):
    operation = operations.get(operator)
    return operation(x,y,n)
    

# Current position 
x,y= 1,1

# 입력받는 공간의 크기 N (1<= N <=100)

n= int(input())

# 여행가 A 가 이동할 계획서 내용 

array = list(input().split())

for a in array:
    x,y=operate(a,x,y,n) 

print(f"X={x},Y={y}")
    




