# enter n
n = int(input())

# number list
num_list = list(map(int, input().split()))[:n]

# result
print(min(num_list), max(num_list))