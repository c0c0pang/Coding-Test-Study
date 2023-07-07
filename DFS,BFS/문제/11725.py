import sys
from collections import deque
n = int(sys.stdin.readline().rstrip())

visited = [False]*(n+1)
box = deque([])
check = [0]*(n+1)
def bfs(n):
    visited[n] = True
    box.appendleft(n)
    
    while len(box):
        v = box.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                box.append(i)
                check[i] = v
                

graph = [
    []
    for _ in range(n+1)
]

for i in range(n-1):
    x,y = map(int,sys.stdin.readline().rstrip().split())
    graph[x].append(y)
    graph[y].append(x)
    

bfs(1)
for i in range(2,n+1):
    print(check[i])