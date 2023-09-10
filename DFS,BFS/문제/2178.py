import sys
from collections import deque

n,m = map(int,sys.stdin.readline().rstrip().split())

graph = [
    list(map(int,sys.stdin.readline().rstrip()))
    for _ in range(n)
]
num = [
    [0]*m
    for _ in range(n)
]
deq = deque()

dx,dy = [-1,1,0,0],[0,0,-1,1]

visited = [
    [False]*(m)
    for _ in range(n)
]
def in_range(nx,ny):
    return nx>=n or nx<0 or ny>=m or ny<0
def bfs():
    deq.appendleft([0,0])
    visited[0][0]=True
    num[0][0] = 1
    while deq:
        sx,sy = deq.popleft()
        for x,y in zip(dx,dy):
            nx=x+sx
            ny=y+sy
            if in_range(nx,ny):
                continue
            if not graph[nx][ny]:
                continue
            if visited[nx][ny]:
                continue
            visited[nx][ny] = True
            num[nx][ny]=num[sx][sy]+1
            deq.append([nx,ny])
            
    return num[n-1][m-1]

print(bfs())