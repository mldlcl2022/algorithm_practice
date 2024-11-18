n,m = map(int, input().split())
a = list(map(int, input().split()))

day = 0
stress = 0
for i in range(n) :
    stress += a[i]
    if stress < 0 : stress = 0
    if stress >= m : day += 1
print(day)