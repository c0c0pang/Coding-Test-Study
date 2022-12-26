import sys

N = int(sys.stdin.readline().rstrip())
x, y = 1, 1

select = list(sys.stdin.readline().rstrip().split())

def in_range(x,y):
    return x>N or x <1 or y>N or y < 1
# dx를 행 dy를 열로 생각하여 좌표값을 정함.
dx = [0,0,-1,1]
dy = [-1,1,0,0]
# 이동하는 커맨드
move_box = ['L','R','U','D']
# 사용자가 입력한 커맨드를 순차적으로 꺼냄
for move in select:
    # 이동하는 커맨드 길이만큼 반복함
    for i in range(len(move_box)):
        # 만약에 같으면 nx(new x,y 에 저장)
        if move == move_box[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # in_range 함수에서 범위 체크 불만족이면 x,y 업데이트 안함
    if in_range(nx,ny):
        continue
    x,y=nx,ny

print(x,y)