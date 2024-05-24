def solution(a):
    
    # 요소와 그 요소의 인덱스를 저장할 딕셔너리
    # O (n)
    index_map = {}
    first_dup=int(1e9)
    index_map={}
    
    for index,value in enumerate(a):
        
        if value in index_map:
            first_dup=min(index,first_dup)
            
        else:
            index_map[value] =index
            
    if first_dup==int(1e9):
        return -1    
    return a[first_dup]
    

