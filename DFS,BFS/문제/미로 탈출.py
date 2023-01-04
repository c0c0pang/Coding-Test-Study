import sys
from collections import deque
n,m = map(int,sys.stdin.readline().rstrip().split())

miro = [
    list(map(int,sys.stdin.readline().rstrip()))
    for _ in range(n)
]
#상,하,좌,우 좌표
dx =[-1,1,0,0]
dy =[0,0,-1,1]

def in_range(x,y):
    return x>=n or x<0 or y>=m or y<0
def bfs(x,y):
    #이동하는 좌표를 queue 로 관리
    queue = deque()
    #처음 0,0 좌표를 대입
    queue.append((x,y))
    #queue 가 없어질 때까지 반복
    while len(queue) !=0:
        #queue의 맨 왼쪽을 꺼냄
        x,y = queue.popleft()
        #4방향이므로 4번 반복하여 상,하,좌,우 이동
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            #조건이 만족하면 다시 탐색
            if in_range(nx,ny) or miro[nx][ny]==0:
                continue
            #최적의 경로를 찾기 위해 이동하는 좌표의 값이 1이면 이전 좌표의 값과 더하고 이를 queue에 대입
            #이렇게 풀면 최적의 값이 나오는 이유는 어느 미로가 주어져도 탈출구 까지 가는 가중치의 값은 무조건 이전의 값 +1 이므로 중간에 다른 길을 가도
            #탈출구로 가는 값에 대해서 영향을 주지 않기 때문이다.
            if miro[nx][ny]==1:
                miro[nx][ny]+=miro[x][y]
                queue.append((nx,ny))
    return miro[n-1][m-1]
print(bfs(0,0))

# for i in range(n):
#     for j in range(m):
#         print(miro[i][j],end=' ')
#     print()