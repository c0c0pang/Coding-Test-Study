import sys

N = int(sys.stdin.readline().rstrip())
array = []
for i in range(N):
    name,num = sys.stdin.readline().rstrip().split()
    array.append([name,int(num)])
#선택정렬
# for i in range(N-1):
#     for j in range(N):
#         if array[i][1] >=array[j][1]:
#             array[i], array[j]= array[j],array[i]
# for i in array:
#     print(i[0],end=' ')
#라이브러리 + 람다 이용
array = sorted(array,key=lambda student: student[1])

for student in array:
    print(student[0],end=' ')