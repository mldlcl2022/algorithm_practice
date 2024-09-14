import sys;input = sys.stdin.readline
n,m = map(int, input().split())
n_list = []
for _ in range(n) :
    n_list.append(int(input()))

min_time = min(n_list);max_time = max(n_list)*m
result = max(n_list)*m
while min_time <= max_time :
    total = 0
    mid = (min_time+max_time) // 2
    for i in range(len(n_list)) :
        total += mid // n_list[i]
    if total >= m :
        max_time = mid - 1
        result = min(result, mid)
    else :
        min_time = mid + 1
print(result)