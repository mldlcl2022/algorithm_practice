import sys;input = sys.stdin.readline
n,m = map(int, input().split())
klist = [int(input()) for _ in range(m)]

result = 0
left = 1;right = max(klist)
while left <= right :
    total = 0
    mid = (left+right)//2
    for i in range(m) :
        total += klist[i]//mid
        if klist[i] % mid != 0 : total += 1
    if total > n : left = mid+1
    else :
        right = mid-1
        result = mid
print(result)