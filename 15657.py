import sys
from itertools import combinations_with_replacement
sys_input = sys.stdin.readline

n,m = map(int,sys_input().split())

nums = list(map(int,sys_input().split()))
nums.sort()
box = list(combinations_with_replacement(nums,m))
for i in box:
    for j in i:
        print(j,end=' ')
    print()