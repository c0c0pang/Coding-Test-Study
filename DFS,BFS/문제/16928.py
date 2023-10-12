import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().rstrip().split())

dic = {}
deq = deque()
for _ in range(n+m):
    x,y = map(int,input().rstrip().split())
    dic[x]=y
dice = [1,2,3,4,5,6]
array = [sys.maxsize]*101
array[1]=0
visited = [False]*101
def bfs():
    deq.append(1)
    visited[1] = True
    while deq:
        now = deq.popleft()
        if now == 100:
            break
        for i in dice:
            s = i+now
            if s>100:
                continue
            if visited[s]:
                continue
            if dic.get(s):
                array[s]=min(array[s],array[now]+1)
                array[dic[s]]=min(array[dic[s]],array[now]+1)
                deq.append(dic[s])
                visited[s]=True
                visited[dic[s]]=True
            else:
                array[s]=min(array[s],array[now]+1)
                deq.append(s)
                visited[s]=True
            
bfs()
print(array[-1])