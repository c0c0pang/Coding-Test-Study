w,h = map(int,input().split())
p,q = map(int,input().split())
t = int(input())

mod_x = (p+t)%(2*w)
mod_y = (q+t)%(2*h)

result_x = w -abs(w-mod_x) 
result_y = h -abs(h-mod_y) 
print(result_x,result_y)