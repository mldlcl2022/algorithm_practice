import sys;input = sys.stdin.readline
import bisect
for _ in range(int(input())) :
    n,m = map(int, input().split())
    a = sorted(list(map(int, input().split()))[:n])
    b = sorted(list(map(int, input().split()))[:m])
    cnt = 0
    for num in b :
        cnt += len(a[bisect.bisect_right(a, num):])
    print(cnt)