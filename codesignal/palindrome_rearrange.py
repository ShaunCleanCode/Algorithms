from collections import Counter

def solution(inputString):
    c=Counter(inputString)
    odd_count=0

    # Even num
    for char in c:
        if c[char] %2!=0:
            odd_count+=1
        
    if odd_count<=1:
        return True
    else :
        return False
                
        
        

