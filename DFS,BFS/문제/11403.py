import sys
from collections import deque
n = int(sys.stdin.readline().rstrip())

graph = [
    list(map(int,sys.stdin.readline().rstrip().split()))
    for _ in range(n)
]
def bfs(start):
    deq = deque()
    deq.appendleft(start)
    visited = [False]*n
    while deq:
        s = deq.popleft()
        for idx,val in enumerate(graph[s]):
            if visited[idx]:
                continue
            if val == 1:
                visited[idx]=True
                graph[start][idx] = 1
                deq.append(idx)
    
for i in range(n):
    bfs(i)
for i in range(n):
    for j in range(n):
        print(graph[i][j],end=" ")
    print()