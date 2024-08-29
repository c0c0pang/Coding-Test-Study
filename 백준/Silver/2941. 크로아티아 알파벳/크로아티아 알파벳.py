arr=['c=','c-','dz=','d-','lj','nj','s=','z=']
s=list(input())
count=0
n=len(s)
for i in arr:
    i=list(i)
    for j in range(n-len(i)+1):
        if i==s[j:j+len(i)]:
            count+=1
print(n-count)
