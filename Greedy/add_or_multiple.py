# 입력값 s
s = input()
result=0
result+=int(s[0])
for i in range(len(s)-1):
    
    if s[i] !='0'or s[i+1] !='0' and result!=0:
        result *=int(s[i+1])
    else:
        result+=int(s[i+1])
        
print(result)