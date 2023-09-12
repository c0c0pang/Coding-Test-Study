import sys
from itertools import combinations
sys_input = sys.stdin.readline

n,m = map(int,sys_input().split())
n_num = 1
m_num = 1

for i in range(n,n-m,-1):
    n_num*=i

for j in range(m,0,-1):
    m_num*=j

print(n_num//m_num)
