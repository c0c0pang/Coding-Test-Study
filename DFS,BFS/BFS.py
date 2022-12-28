import sys
from collections import deque

def bfs(graph,n,visited):
    visited[n] = True
    box.appendleft(n)
    while len(box) !=0 :
        v = box.popleft()
        print(v,end=' ')
        for i in graph[v]:
            if not(visited[i]):
                box.append(i)
                visited[i] = True
box = deque([])

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



visited = [False]*len(graph)

bfs(graph,1,visited)