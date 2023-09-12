import sys
t = int(sys.stdin.readline().rstrip())

array = [
    {}
    for _ in range(t)
]
for i in range(t):
    seen = []
    n = int(sys.stdin.readline().rstrip())
    n1, n2 = [], []
    result = []
    num = 1
    for j in range(n):
        f, c = sys.stdin.readline().rstrip().split()
        n1.append(f)
        n2.append(c)
        array[i][c] = []
    for key, value in zip(n1, n2):
        if key not in seen:
            seen.append(key)
            array[i][value] += [key]
    for k,v in array[i].items():
        result.append(v)
    for last in result:
        num *=len(last)+1
    print(num-1)
