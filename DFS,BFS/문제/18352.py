import sys
from collections import deque
n,m,k,x = map(int,sys.stdin.readline().rstrip().split())
graph =[
    []
    for _ in range(n+1)
]
for _ in range(m):
    A,B = map(int,sys.stdin.readline().rstrip().split())
    graph[A].append(B)
    
visited_num = [0]*(n+1)
visited = [False]*(n+1)
queue = deque()
def bfs(graph,x,visited):
    queue.append(x)
    visited[x] = True
    while len(queue):
        v = queue.popleft()
        for n in graph[v]:
            if not visited[n]:
                visited_num[n]=visited_num[v]+1
                visited[n] = True
                queue.append(n)
            
bfs(graph,x,visited)
check = False
for i in range(1,n+1):
    if visited_num[i]==k:
        print(i)
        check = True
if not check:
    print(-1)
        