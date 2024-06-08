t = int(input())
for _ in range(t) :
    r,s = input().split()
    for a in s[:20] : print(a*int(r), end= '')
    print()