# 무한을 의마하는 값으로 10억을 설정
INF =int(1e9) 

# 노드의 개수 , 및 엣지의 개수를 입력받기
n,m= map(int,input().split())

# 2차원 리스트를 만들고 모든 값을 무한으로 초기화
graph =[[INF]*(n+1)for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            graph[i][j]=0
            
for _ in range(m):
    a,b = map(int,input().split())
    graph[a][b]=1
    graph[b][a]=1
    
    
x,k =map(int,input().split())

for middle in range(1,n+1):
    for start in range(1,n+1):
        for end in range(1,n+1):
            graph[start][end] = min(graph[start][end],graph[start][middle]+graph[middle][end])
            
distance =graph[1][k]+ graph[k][x]

if distance>=INF:
    print("-1")
else:
    print(distance)
            