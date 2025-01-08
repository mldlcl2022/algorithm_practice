n = int(input())
s = list(map(int, input().split()))
m = max(s)
total = 0
for i in range(len(s)) :
    total += (s[i]/m*100)
print(total/n)