import sys;input = sys.stdin.readline
k,n = map(int, input().split())
lines = []
for _ in range(k) :
    lines.append(int(input()))

left = 1
right = max(lines)
lines.sort()
while left <= right :
    center = (left+right) // 2
    cnt = sum([line//center for line in lines])
    if cnt >= n : left = center+1
    else : right = center-1
print(right)