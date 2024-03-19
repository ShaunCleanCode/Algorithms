

# 현재위치
array =list(map(int,input().split()))
x =array[0]
y=array[1]

count =0
if(x-2) >=1 and (y-1) >=1:
    count+=1
if(x-2) >=1 and (y+1) <=8:
    count+=1
if(x+2) <=8 and (y+1) <=8:
    count+=1
if(x+2) <=8 and (y-1)>=1:
    count+=1
    
if(x-1) >=1 and (y+2) <=8:
    count+=1
if(x-1) >=1 and (y-2) >=1:
    count+=1
if(x+1) <=8 and (y-2) >=1:
    count+=1
if(x+1) <=8 and (y+2) <=8:
    count+=1
print(count)
