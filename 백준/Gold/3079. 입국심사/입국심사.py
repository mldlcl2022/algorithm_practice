import sys;input = sys.stdin.readline
n,m = map(int, input().split())
tables = []
for _ in range(n) :
    tables.append(int(input()))

min_time = min(tables)
max_time = result = max(tables)*m
while min_time <= max_time :
    mid = (min_time+max_time)//2
    if sum([mid//table for table in tables]) >= m :
        max_time = mid-1
        result = min(mid, result)
    else :
        min_time = mid+1
print(result)