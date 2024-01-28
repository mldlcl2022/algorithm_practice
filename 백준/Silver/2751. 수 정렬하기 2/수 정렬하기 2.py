import sys

n = int(sys.stdin.readline())

num_list = []
for i in range(n) :
    num = int(sys.stdin.readline())
    num_list.append(num)

for num in sorted(num_list) :
    print(num)