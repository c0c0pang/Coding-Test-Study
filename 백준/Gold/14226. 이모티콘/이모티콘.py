import sys
from collections import deque
input = sys.stdin.readline

s = int(input())

visitied = [[False]*(s+1) for _ in range(s+1)]
def bfs():
    queue = deque([(1,0,0)])
    while queue:
        cnt,seconds,clipboard = queue.popleft()
        if(cnt>s or clipboard>s):
            continue
        if cnt == s:
            print(seconds)
            break
        if visitied[cnt][clipboard]:
            continue
        visitied[cnt][clipboard] = True
        seconds+=1
        
        #복사
        queue.append((cnt,seconds,cnt))
        #붙여넣기
        sum_num=clipboard+cnt
        queue.append((sum_num,seconds,clipboard))
        #삭제
        if cnt>2:
            cnt-=1
            queue.append((cnt,seconds,clipboard))
        
bfs()



