import sys
from collections import deque
n,m = map(int,sys.stdin.readline().rstrip().split())

graph = [
    []
    for _ in range(n+1)
]
result = []
def bfs(n,visited,number):
    deq = deque()
    deq.appendleft(n)
    visited[n] = True
    ##한꺼번에 풀지말고 하나씩 pop해보자
    while deq:
        s = deq.popleft()
        for i in graph[s]:
            if visited[i]:
                continue
            number[i] = number[s]+1
            deq.append(i)
            visited[i] = True
    return sum(number),n

for _ in range(m):
    x,y = map(int,sys.stdin.readline().rstrip().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(1,n+1):
    visited = [False]*(n+1)
    number = [0]*(n+1)
    result.append(bfs(i,visited,number))
    
print(min(result)[1])
    