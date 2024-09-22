import sys;input = sys.stdin.readline
import bisect
t = int(input())
n = int(input())
a = list(map(int, input().split()))[:n]
m = int(input())
b = list(map(int, input().split()))[:m]

asum = a
for i in range(n) :
    tmp = a[i]
    for j in range(i+1,n) :
        tmp += a[j]
        asum.append(tmp)
bsum = b
for i in range(m) :
    tmp = b[i]
    for j in range(i+1,m) :
        tmp += b[j]
        bsum.append(tmp)

asum.sort();bsum.sort()
result = 0
for i in range(len(asum)) :
    left = bisect.bisect_left(bsum, t-asum[i])
    right = bisect.bisect_right(bsum, t-asum[i])
    result += (right - left)
print(result)