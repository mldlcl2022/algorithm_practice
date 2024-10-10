import sys;input = sys.stdin.readline
n = int(input())
stack = []
for _ in range(n) :
    stack.append(int(input()))
cnt = 0
bar = 0
for i in range(n) :
    if i == 0 :
        cnt += 1
        bar = stack.pop()
    else :
        pop_num = stack.pop()
        if pop_num > bar :
            cnt += 1
            bar = pop_num
print(cnt)