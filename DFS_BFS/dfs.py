# Representing connected Nodes information
graph = [
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


def dfs(graph,v,visited):
    visited[v]=True
    print(f"Visited :{v}",end=" ")
    for i in graph[v]:
        if visited[i]==False:
            dfs(graph,i,visited)
            
            

# Representing visited information for each Nodes
visited =[False]* 9

dfs(graph,1,visited)