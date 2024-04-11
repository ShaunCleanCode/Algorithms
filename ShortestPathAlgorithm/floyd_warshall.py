INF =int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수 및 간선의 개수를 입력받기 
n=int(input())
m=int(input())
# 2차원 리스트(그래프 표현)를 만들고 무한으로 초기화

graph =[[INF]* (n+1)for _ in range(n+1)]


for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            graph[i][j]=0


for _ in range(m):
    a,b,c =map(int,input().split())
    graph[a][b]=c
    
# 점화식에 따라 플로이드 워설 알고리즘을 수행
for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])
            
