def solution(matrix):
    dx=[1,0,-1,0,1,1,-1,-1]
    dy=[0,1,0,-1,1,-1,1,-1]
    col_n=len(matrix)
    row_n= len(matrix[0])
    mine_sweeper=[[0 for i in range(row_n)] for j in range(col_n)]
    
    
    
    for i in range(col_n):
        for j in range(row_n):
            for k in range(8):
                if 0<= i +dx[k] <col_n and 0<= j+dy[k] <row_n:
                    mine_sweeper[i][j]+=matrix[i+dx[k]][j+dy[k]]
                    
    return mine_sweeper
        
    
           
            
