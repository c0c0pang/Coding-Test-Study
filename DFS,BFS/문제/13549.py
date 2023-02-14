import sys
from collections import deque
box = deque([])
n, k = map(int, sys.stdin.readline().rstrip().split())
visited = [False]*(200003)
graph = [0]*200003


def bfs(n):
    box.appendleft(n)
    global result
    result = sys.maxsize
    while len(box):
        v = box.popleft()
        if k == v:
            result = min(result, graph[k])
        if v >= 100002 or v < 0:
            continue
        if not visited[v*2]:
            graph[v*2] = graph[v]
            box.append(v*2)
            visited[v*2] = True
        if not visited[v-1]:
            graph[v-1] = graph[v]+1
            box.append(v-1)
            visited[v-1] = True
        if not visited[v+1]:
            graph[v+1] = graph[v]+1
            box.append(v+1)
            visited[v+1] = True


bfs(n)
print(result)
