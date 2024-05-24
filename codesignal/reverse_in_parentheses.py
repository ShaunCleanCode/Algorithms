def solution(inputString):
    #1. (  eend ) go recursive
    #2. 
    stack=[]
    chars=list(inputString)
    for i,char in enumerate(chars):
        
        if char =="(":
            stack.append(i+1)
            
        elif char==")":
            start =stack.pop()
            chars[start:i] =chars[start:i][::-1]
            
    return ''.join(char for char in chars if char not in ["(",")"])
            
            
        
            


