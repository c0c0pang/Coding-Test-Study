import sys
N = int(sys.stdin.readline().rstrip());
# 범위 벗어나는 구간을 체크해주는 함수
def in_range(num):
    # N x N 범위를 넘은 경우
    if(num > N):
        return False
    if(num == 0):
        return False
    
    return True

select = list(sys.stdin.readline().rstrip().split());

X = 1;
Y = 1;

for M in select:
    if(M == 'L'and in_range(Y-1)):
        Y -= 1;
    if(M == 'R'and in_range(Y+1)):
        Y += 1;
    if(M == 'U'and in_range(X-1)):
        X -=1;
    if(M == 'D'and in_range(X+1)):
        X +=1;
        
print(X,Y);

    
        