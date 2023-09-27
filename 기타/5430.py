import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

def parsing(x):
    if(x=='[]'):
        s = []
    else:
        s = x[1:-1].split(',')
    return s
def result(target,p):
    check = True
    reverse = 0
    s = deque(target)
    for i in p:
        if i == 'R':
            reverse+=1
        else:
            if len(s) == 0:
                check = False
                break
            else:
                if reverse%2==0:
                    s.popleft()
                else:
                    s.pop()
    if not check:
        return 'error'
    if reverse%2==0:
        r = ','.join(s)
        return '['+r+']'
    else:
        s.reverse()
        r = ','.join(s)
        return '['+r+']'
for _ in range(T):

    p = input().rstrip()

    n = int(input())

    x = input().rstrip()
    print(result(parsing(x),p))