import sys
from itertools import combinations
sys_input = sys.stdin.readline

n,m = map(int,sys_input().split())

array = [
    i
    for i in range(1,n+1)
]

box = list(combinations(array,m))
for i in box:
    for j in i:
        print(j,end=" ")