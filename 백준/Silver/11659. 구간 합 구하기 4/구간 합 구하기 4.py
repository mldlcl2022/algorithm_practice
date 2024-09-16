import sys;input = sys.stdin.readline
n, m = map(int, input().split())
nums = list(map(int, input().split()))[:n]
cumsum = 0
cumsum_list = [0]
for num in nums :
    cumsum += num
    cumsum_list.append(cumsum)
for _ in range(m) :
    i,j = map(int, input().split())
    print(cumsum_list[j]-cumsum_list[i-1])