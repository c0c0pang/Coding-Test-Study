import sys

n,m = map(int,sys.stdin.readline().rstrip().split())
box =[
    list(map(int,sys.stdin.readline().rstrip()))
    for _ in range(n)
]

def in_range(x,y):
    return x>=n or x<0 or y>=m or y<0
def dfs(x,y):
    if in_range(x,y):
        return False
    if box[x][y] ==0:
        box[x][y]=1
        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        return True
    return False
result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j)==True:
            result+=1
print(result)