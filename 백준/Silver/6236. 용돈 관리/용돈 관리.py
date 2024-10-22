import sys;input = sys.stdin.readline
n,m = map(int, input().split())
day_money = [int(input()) for _ in range(n)]

left = min(day_money);right = sum(day_money)
while left <= right :
    mid = (left+right)//2
    cnt = 1
    tmp = mid
    for money in day_money :
        if tmp - money < 0 :
            tmp = mid
            cnt += 1
        tmp -= money
    if cnt > m or mid < max(day_money) :
        left = mid+1
    else :
        right = mid-1
        result = mid
print(result)