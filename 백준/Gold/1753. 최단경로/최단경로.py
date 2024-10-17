import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)
v,e = map(int,input().split())
k = int(input())
grahp = [[] for _ in range(v+1)]
distance = [INF]*(v+1)
for _ in range(e):
    u,v,w = map(int,input().split())
    grahp[u].append((v,w))

def Dijkstra(start):       
    hq = []
    heapq.heappush(hq,(0,start))
    distance[start] = 0
    
    while hq:
        dist,now = heapq.heappop(hq)
        if distance[now] < dist:
            continue
        for i in grahp[now]:
            nv,nw = i
            cost = nw + dist
            if cost <distance[nv]:
                heapq.heappush(hq,(cost,nv))
                distance[nv] = cost
            
        
Dijkstra(k)

for i in range(1,len(distance)):
    if distance[i] == INF:
        print('INF')
        continue
    print(distance[i])