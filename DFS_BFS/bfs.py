from collections import deque
# Representing connected Nodes information 
graph =[
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
    
]

queue =[]

# Visited information for each nodes
visited= [False] * 9



# BFS
def bfs(graph,start,visited):
    # Using deque Library for implement queue
    queue=deque([start])
    # Visited current Node 
    visited[start]=True
    # Recursive and stop condition is queue empty.
    while queue:
        v= queue.popleft()
        # pick 
        print(v,end=' ')
        # Visited an Unvisited Adjacent Node 
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True
    
    
bfs(graph,1,visited)
    



