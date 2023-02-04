import sys
from collections import deque

t = int(sys.stdin.readline().rstrip())

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def in_range(nx, ny):
    return nx < 0 or nx >= m or ny < 0 or ny >= n


def bfs(visited, array):
    cnt = 0
    for idx, val in enumerate(array):
        for v in val:
            if not visited[idx][v]:
                visited[idx][v] = True
                box_x.appendleft(idx)
                box_y.appendleft(v)
                while len(box_x) and len(box_y):
                    x = box_x.popleft()
                    y = box_y.popleft()
                    for n1, n2 in zip(dx, dy):
                        nx = x + n1
                        ny = y + n2
                        if in_range(nx, ny):
                            continue
                        if check[nx][ny] == 0:
                            continue
                        if not(visited[nx][ny]):
                            box_x.append(nx)
                            box_y.append(ny)
                            visited[nx][ny] = True
                cnt += 1
    return cnt


box_x = deque([])
box_y = deque([])

for _ in range(t):
    global m, n

    m, n, k = map(int, sys.stdin.readline().rstrip().split())

    visited = [
        [False]*n
        for _ in range(m)
    ]
    array = [
        []*n
        for _ in range(m)
    ]
    check = [
        [0]*n
        for _ in range(m)
    ]

    for _ in range(k):
        x, y = map(int, sys.stdin.readline().rstrip().split())
        array[x].append(y)
        check[x][y] = 1
    print(bfs(visited, array))
