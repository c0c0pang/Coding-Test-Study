import sys

N,M,K = map(int,sys.stdin.readline().rstrip().split());

box = list(map(int,sys.stdin.readline().rstrip().split()));

box.sort();
#첫번째로 큰 수
first = box[N-1]; 
#두번째로 큰 수
second = box[N-2];
#예시
#5 8 3 
#2 4 5 4 6
#6665 6665

count = 0;

#전체 반복 횟수에서 큰 수와 두번째 큰수가 반복되는 길이는 K+1 이므로 이를 나눠주고 큰 수의 반복횟수를
#곱해주면 총 큰 수의 반복 횟수가 나온다.
count += int(M/(K+1))*K;

#M이 K+1로 나눴을 때 나누어 떨어지지 않는 경우를 고려
count += M%(K+1);

result = 0;
#가장 큰 수의 합
result += first*count;
#두번째로 큰 수의 합
result += second*(M-count);

print(result);