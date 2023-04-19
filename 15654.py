import sys
from itertools import permutations
sys_input = sys.stdin.readline

n,m = map(int,sys_input().split())

nums = list(map(int,sys_input().split()))
nums.sort()
box = list(permutations(nums,m))
for i in box:
    for j in i:
        print(j,end=' ')
    print()