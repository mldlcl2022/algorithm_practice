# enter n
n = int(input())

# enter num
num = input()

# number list
num_list = []
for i in range(n) :
    num_list.append(int(num.split()[i]))

# enter v
v = int(input())

# result
print(num_list.count(v))