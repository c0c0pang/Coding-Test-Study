import sys

input = sys.stdin.readline

n,m = input().split()

number = int(m+n)
n = int(n)
check = False
for i in range(2,number):
    if(number%i == 0):
        check = True
        break
for i in range(2,n):
    if(n%i == 0):
        check = True
        break
if(check):
    print("No")
else:
    print("Yes")