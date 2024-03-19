# 입력값 정수 N
n= int(input())
count=0
for k  in range(0,n+1):
    if '3' in str(k):
        count +=3600
        print(count)
        continue    
    for i in range(0,60):
        if '3' in str(i):
            count +=60
            print(count)
            continue
        for j in range(0,60):
            if '3' in str(j):
                count +=1
                print(count)
                continue
print(count)
    
         
        
        



