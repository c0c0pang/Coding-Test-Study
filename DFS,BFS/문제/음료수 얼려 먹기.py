# 탐색을 처음부터 끝까지 이어지는 것이 아닌 특정 부분을 탐색하고 또 다른 부분을 탐색하는 경우 dfs가 유리
import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

graph = [
    list(map(int, sys.stdin.readline().rstrip()))
    for _ in range(n)
]


def in_range(x, y):
    return x >= n or x < 0 or y >= m or y < 0


def dfs(x, y):
    if in_range(x, y):
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x, y-1)
        return True
    return False


result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)
