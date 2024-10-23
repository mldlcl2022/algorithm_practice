import sys;input = sys.stdin.readline
n,k = map(int, input().split())
a = sorted([int(input()) for _ in range(n)], reverse= True)

cnt = 0
for coin in a :
    if k == 0 : break
    elif coin > k : continue
    elif k % coin == 0 :
        cnt += k//coin
        k -= (k//coin)*coin
    else :
        cnt += k//coin
        k -= (k//coin)*coin
print(cnt)