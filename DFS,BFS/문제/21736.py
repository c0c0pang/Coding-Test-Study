import sys
from collections import deque


n,m = map(int,sys.stdin.readline().rstrip().split())

array = [
    list(sys.stdin.readline().rstrip())
    for _ in range(n)
]

deq = deque([])
visited=[
    [False]*m
    for _ in range(n)
]
def in_range(nx,ny):
    return nx>=n or ny>=m or nx<0 or ny<0

dx,dy=[-1,1,0,0],[0,0,-1,1]

def bfs(ix,iy):
    deq.appendleft([ix,iy])
    cnt=0
    visited[ix][iy]=True
    while len(deq) !=0:
        wx,wy = deq.popleft()
        for x,y in zip(dx,dy):
            nx,ny = wx+x,wy+y
            if in_range(nx,ny):
                continue
            if visited[nx][ny]:
                continue
            if array[nx][ny]=='X':
                continue
            visited[nx][ny]=True
            if array[nx][ny]=='O':
                deq.append([nx,ny])
            if array[nx][ny]=='P':
                cnt+=1
                deq.append([nx,ny])
    if(cnt==0):
        return 'TT'
    return cnt
for i in range(n):
    for j in range(m):
        if array[i][j]=='I':
            print(bfs(i,j))
            exit()
