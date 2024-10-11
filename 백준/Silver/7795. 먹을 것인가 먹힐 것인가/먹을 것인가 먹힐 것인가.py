import sys;input = sys.stdin.readline
for _ in range(int(input())) :
    n,m = map(int, input().split())
    a = sorted(list(map(int, input().split()))[:n])
    b = sorted(list(map(int, input().split()))[:m])
    cnt = 0
    pair = 0
    for i in range(n) :
        while True :
            if cnt == m or a[i] <= b[cnt] :
                pair += cnt
                break
            else : cnt += 1
    print(pair)