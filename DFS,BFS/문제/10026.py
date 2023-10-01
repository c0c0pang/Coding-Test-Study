import sys
from collections import deque
input = sys.stdin.readline

n = int(input().rstrip())

array = [
    list(input().rstrip())
    for _ in range(n)
]
dx,dy=[-1,1,0,0],[0,0,-1,1]
visited_1 = [
    [False]*n
    for _ in range(n)
]
visited_2 = [
    [False]*n
    for _ in range(n)
]
def in_range(nx,ny):
    return nx>=n or nx<0 or ny>=n or ny<0
cnt_1 = 0
cnt_2 = 0
def bfs_1(color,target_x,target_y):
    global check,cnt_1
    deq = deque()
    deq.appendleft([target_x,target_y])
    visited_1[target_x][target_y] = True
    while deq:
        x,y = deq.popleft()
        for sx,sy in zip(dx,dy):
            nx = x+sx
            ny = y+sy
            if in_range(nx,ny):
                continue
            if visited_1[nx][ny]:
                continue
            if array[nx][ny]==color:
                visited_1[nx][ny]=True
                deq.append([nx,ny])
    cnt_1+=1
def bfs_2(color,target_x,target_y):
    global check,cnt_2
    deq = deque()
    deq.appendleft([target_x,target_y])
    visited_2[target_x][target_y] = True
    check = False
    while deq:
        x,y = deq.popleft()
        for sx,sy in zip(dx,dy):
            nx = x+sx
            ny = y+sy
            if in_range(nx,ny):
                continue
            if visited_2[nx][ny]:
                continue
            if array[nx][ny]==color:
                visited_2[nx][ny]=True
                deq.append([nx,ny])
            if color == 'R' and array[nx][ny]=='G':
                visited_2[nx][ny]=True
                deq.append([nx,ny])
            if color == 'G' and array[nx][ny]=='R':
                visited_2[nx][ny]=True
                deq.append([nx,ny])
            
    cnt_2+=1
for i in range(n):
    for j in range(n):
        if array[i][j] == 'R':
            if visited_1[i][j]:
                continue
            bfs_1('R',i,j)
            if visited_2[i][j]:
                continue
            bfs_2('R',i,j)
        if array[i][j] == 'B':
            if visited_1[i][j]:
                continue
            bfs_1('B',i,j)
            if visited_2[i][j]:
                continue
            bfs_2('B',i,j)
        if array[i][j] == 'G':
            if visited_1[i][j]:
                continue
            bfs_1('G',i,j)
            if visited_2[i][j]:
                continue
            bfs_2('G',i,j)
print(cnt_1,cnt_2)