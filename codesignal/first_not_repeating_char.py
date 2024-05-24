def solution(s):
    # 
    index_map={}
    for index,char in enumerate(s):
        
        if char in index_map:
            index_map[char]=1
            
        else:
            index_map[char]=0
            
    
    for char in s:
        if index_map[char]==0:
            return char
            
    return "_"



def solution(s):
    for c in s:
        if s.index(c) == s.rindex(c):
            return c
    return '_'
        
