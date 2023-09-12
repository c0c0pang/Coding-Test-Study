import sys

n = int(sys.stdin.readline().rstrip())
array = [
    list(map(int, sys.stdin.readline().rstrip().split()))
    for _ in range(n)
]

result_w, result_b = 0, 0


def slice(s1, s2, x, y):
    global result_w, result_b
    w = 0
    b = 0
    for i in range(x, s1):
        for j in range(y, s2):
            if array[i][j] == 0:
                w += 1
            else:
                b += 1
    if w == 0:
        result_b += 1
        return result_w, result_b
    elif b == 0:
        result_w += 1
        return result_w, result_b
    else:
        slice(((x+s1)//2), ((y+s2)//2), x, y)  # 1사분면
        slice((s1//2)+(x//2), s2, x, (s2//2)+(y//2))  # 2사분면
        slice(s1, ((y+s2)//2), (s1//2)+(x//2), y)  # 3사분면
        slice(s1, s2, (s1//2)+(x//2), (s2//2)+(y//2))  # 4사분면
    return result_w, result_b


result_w, result_b = slice(n, n, 0, 0)
print(result_w)
print(result_b)
