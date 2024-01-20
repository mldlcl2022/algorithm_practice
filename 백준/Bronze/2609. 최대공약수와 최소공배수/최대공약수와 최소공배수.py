n,m = map(int,input().split())

a = []
for i in range(1,max(n,m)+1) :
    if n%i == 0 and m%i == 0 :
        a.append(i)
print(max(a))
print(max(a) * (n//max(a)) * (m//max(a)))