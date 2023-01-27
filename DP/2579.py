import sys

n = int(sys.stdin.readline().rstrip())

array = [
     int(sys.stdin.readline().rstrip())
    for _ in range(n)
]
dp = [
    [{0: 0},{0:0}]
    for _ in range(n+1)
]
dp[1] = [{1: array[0]},{0:0}]
for i in range(2, n+1):
    for j in dp[i-1]:
        for key, value in  j.items():
            if key+1 <=2:
                for x,y in dp[i][0].items():
                    if y<value+array[i-1]:
                        dp[i][0] = {key+1: value+array[i-1]}
    for j in dp[i-2]:
        for key, value in j.items():
            for x,y in dp[i][1].items():
                dp[i][1] = {1: max(y,value+array[i-1])}

result = 0
for i in dp[n]:
    for key,value in i.items():
        result = max(result,value)

print(result)