n,k = map(int, input().split())
num = 0
cnt = 0
for i in range(1,n+1) :
    if n % i == 0 :
        cnt += 1
        num = i
    if cnt == k : break
if cnt < k : print(0)
else : print(num)