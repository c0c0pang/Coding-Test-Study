import sys
from collections import deque
n, m, v = map(int, sys.stdin.readline().rstrip().split())


def dfs(graph, v, visited):
    if not visited[v]:
        visited[v] = True
        print(v, end=' ')
        for i in graph[v]:
            dfs(graph, i, visited)
    else:
        return


def bfs(graph, v, visited):
    visited[v] = True
    box.appendleft(v)

    while len(box):
        s = box.popleft()
        print(s, end=' ')
        for i in graph[s]:
            if not visited[i]:
                visited[i] = True
                box.append(i)


graph = [
    []
    for _ in range(n+1)
]

box = deque([])


for _ in range(m):
    n1, n2 = map(int, sys.stdin.readline().rstrip().split())
    graph[n1].append(n2)
    graph[n2].append(n1)
    graph[n1].sort()
    graph[n2].sort()

visited_d = [False]*(len(graph))
visited_b = [False]*(len(graph))

dfs(graph, v, visited_d)
print()
bfs(graph, v, visited_b)
