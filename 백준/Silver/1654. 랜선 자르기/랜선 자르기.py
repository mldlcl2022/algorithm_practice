k, n = map(int, input().split())
l = []
for _ in range(k) :
    l.append(int(input()))

min_length = 1;max_length = max(l)
while min_length <= max_length :
    mid_length = (min_length + max_length) // 2
    num = sum([i//mid_length for i in l])
    if num >= n : min_length = mid_length + 1
    else : max_length = mid_length - 1
print(max_length)