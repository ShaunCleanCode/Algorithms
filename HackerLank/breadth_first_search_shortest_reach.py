#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque
#
# Complete the 'bfs' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. 2D_INTEGER_ARRAY edges
#  4. INTEGER s
#

def bfs(n, m, edges, s):
    graph = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    distance = [-1] * (n + 1)  # 모든 거리를 -1로 초기화

    for e in edges:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])  # 양방향으로 그래프 생성

    queue = deque([(s, 0)])  # 시작 노드와 거리
    visited[s] = True
    distance[s] = 0  # 시작 노드의 거리는 0

    while queue:
        node, dist = queue.popleft()

        for connect in graph[node]:
            if not visited[connect]:
                visited[connect] = True
                queue.append((connect, dist + 6))
                distance[connect] = dist + 6  # 이웃 노드에 대한 거리 업데이트

    # 시작 노드 자신을 제외하고 거리 리스트 반환
    return [distance[i] if i != s else -1 for i in range(1, n + 1)]


        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input().strip())

        result = bfs(n, m, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')
        

    fptr.close()
