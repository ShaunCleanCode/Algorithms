import sys
import heapq
input =sys.stdin.readline
INF=int(1e9)   # 무한을 의미하는 값 10억 


# 노드의 개수 ,엣지의 개수 입력받기

n,m=map(int,input().split())

start =int(input())

graph =[[]for i in range (n+1)]


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
        # 이 아래 부분 추가 설명좀 해줄래?
        if distance[now] <dist:
            continue
        for i in graph[now]:
            cost =dist +i[1]
            if cost <distance[i[0]]:
                distance[i[0]] =cost
                heapq.heappush(q,(cost,i[0]))
                
                
for i in range(1, n+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])