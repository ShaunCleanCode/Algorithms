import heapq

INF=int(1e9)
# 도시의 개수 N , 통로의 개수 M , 시작 노드 start
n,m,start=map(int,input().split())

# 그래프 초기화
graph=[[]for i in range(n+1)]

distance =[INF]*(n+1)

for _ in range(m):
    a,b,c =map(int,input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        dist,now =heapq.heappop(q)
        if distance[now] <dist:
            continue
        for i in graph[now]:
            cost =dist +i[1]
            if cost <distance[i[0]]:
                distance[i[0]] =cost
                heapq.heappush(q,(cost,i[0]))
                

            
            
dijkstra(start)

count =0
max_distance=0
for i in range(1,n+1):
    if distance[i]!=INF:
        count+=1
        max_distance=max(max_distance,distance[i])
           
print(str(max_distance)+" "+str(count-1))
           


## 특정노드에서 다른 노드들까지 간다면? 다익스트라 알고리즘 
    
