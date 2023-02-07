import sys
from collections import deque
n, m = map(int, sys.stdin.readline().rstrip().split())

visited = [False]*(n+1)

box = deque([])


def bfs(visited, graph):
    cnt = 0
    result = 0
    global check
    check = False
    if m > 0:
        for i in graph:
            check = False
            for j in i:
                visited[j] = True
                box.appendleft(j)
                while len(box):
                    v = box.popleft()
                    for z in graph[v]:
                        if not visited[z]:
                            visited[z] = True
                            check = True
                            box.append(z)
            if check:
                result += 1
    else:
        return n
    for i in range(1, len(visited)):
        if visited[i]:
            cnt += 1
    return (n-cnt)+result


graph = [
    []
    for _ in range(n+1)
]
for _ in range(m):
    u, v = map(int, sys.stdin.readline().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)
print(bfs(visited, graph))
