import sys
import math
input = sys.stdin.readline
n1,n2,n3 = map(int,input().split())

result_1 = math.floor(n1*(n2/n3))
result_2 = math.floor((n1/n2)*n3)

answer = max(result_1,result_2)
print(answer)
        
    


