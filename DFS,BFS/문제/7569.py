import sys
from collections import deque
input = sys.stdin.readline
M,N,H = map(int,input().rstrip().split())
#2차원으로 풀면 층을 넘나들 수 있는 버그 발생
box = [
    [
        list(map(int,input().rstrip().split()))
        for _ in range(N)
    ]
    for _ in range(H)
]
def in_range(nx,ny,nz):
    return nx>=N or nx<0 or ny>=M or ny<0 or nz>=H or nz<0
visited = [
    [
        [False]*M
        for _ in range(N)
    ]
    for _ in range(H)
]
dx,dy = [-1,1,0,0],[0,0,-1,1]
dz = [-1,1]
deq = deque([])
def bfs():
    global max_num, min_num
    max_num = -sys.maxsize
    min_num = sys.maxsize
    while deq:
        h,c,r = deq.popleft()
        for x,y in zip(dx,dy):
            nx = x+c
            ny = y+r
            if in_range(nx,ny,h):
                continue
            if visited[h][nx][ny]:
                continue
            if box[h][nx][ny]>=0:
                box[h][nx][ny] = box[h][c][r] + 1
                visited[h][nx][ny] = True
                deq.append([h,nx,ny])
                min_num = min(min_num,box[h][nx][ny])
                max_num = max(max_num,box[h][nx][ny])
        for z in dz:
            nz = h+z
            if in_range(c,r,nz):
                continue
            if visited[nz][c][r]:
                continue
            if box[nz][c][r]>=0:
                box[nz][c][r] = box[h][c][r] + 1
                visited[nz][c][r] = True
                deq.append([nz,c,r])
                min_num = min(min_num,box[nz][c][r])
                max_num = max(max_num,box[nz][c][r])
def result():
    global check
    check = True
    if cnt == H*N*M:
        return -1
    for i in range(H):
        for j in range(N):
            for z in range(M):
                if visited[i][j][z] == False:
                    check = False
    if not check:
        return -1
    if max_num == -sys.maxsize and min_num == sys.maxsize:
        return 0
    return max_num
cnt = 0
for i in range(H):
    for j in range(N):
        for z in range(M):
            if box [i][j][z] == 0:
                cnt+=1
            if box[i][j][z] == 1:
                deq.append([i,j,z])
                visited[i][j][z] = True
                box[i][j][z] = 0
            if box[i][j][z] == -1:
                visited[i][j][z] = True
bfs()
print(result())