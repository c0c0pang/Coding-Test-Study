import sys

#(A,B) A = 북쪽으로부터 떨어진 칸의 개수, B = 서쪽으로부터 떨어진 칸의 개수

N,M = map(int,sys.stdin.readline().rstrip().split())

A,B,d = map(int,sys.stdin.readline().rstrip().split())

# 0:북쪽,3:서쪽,2:남쪽,1:동쪽
dx = [-1,0,1,0]
dy = [0,-1,0,1]
# 북 -> 서, 서 -> 남, 남 -> 동, 동->북 ... 
def in_range(nx,ny):
    return nx>M or nx<1 or ny>N or ny <1
count = 1;
limit = 0;
map_box = [
    list(map(int,sys.stdin.readline().rstrip().split()))
    for _ in range(M)
]
map_box[A][B]=2

last = False

while True:    
    if limit ==4 and last:
        break
    if limit == 4:
        A = A + dx[d-2]
        B = B + dy[d-2]
        print('뒤로 이동:',A,B)
        if(map_box[A][B]==1):
            break
        last = True;
        limit = 0;
    d +=1
    if d == 4:
        d = 0
    nx = A + dx[d]
    ny = B + dy[d]
    print("이동:",nx,ny);
    print("이동,바라보는방향:",d)
    if in_range(nx,ny) or map_box[nx][ny] == 1 or map_box[nx][ny] ==2:
        limit +=1
        continue
    map_box[nx][ny]=2
    A,B=nx,ny
    limit = 0;
    count+=1
    print("도착:",A,B);
    print("도착,바라보는방향:",d)
print(count);