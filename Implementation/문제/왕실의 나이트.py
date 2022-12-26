import sys

# (2,1),(2,-1),(-2,1),(-2,-1)
# (1,2),(1,-2),(-1,2),(-1,-2)

select = sys.stdin.readline().rstrip()

N = 8; # 최대 행
M = 8; # 최대 열

#체스판에서 이동할 수 있는 좌표쌍
dx = [2,2,-2,-2,1,1,-1,-1]#행
dy = [1,-1,1,-1,2,-2,2,-2]#열

def in_range(nx,ny):
    return nx > N or nx <1 or ny > M or ny <1

move_box = ['a','b','c','d','e','f','g','h'] #체스판 알파벳

count = 0;
# 1열 부터 8열 탐색
for i in range(1,len(move_box)+1):
    # 사용자가 입력한 체스판이 어느 좌표에서 시작하는지 체크
    if move_box[i-1] in select:
        # a1 이면 1 이 행
        x = int(select[1])
        # 입력과 같은 체스판이 있는 열
        y = i
        # 총 이동할 수 있는 8가지를 전부 체크
        for j in range(len(move_box)):
            nx = x + dx[j]
            ny = y + dy[j]
            # in_range 함수를 통해 범위를 벗어나는지 체크
            if in_range(nx,ny):
                continue
            # 범위안에 들어오면 카운팅
            count+=1;

print(count);
