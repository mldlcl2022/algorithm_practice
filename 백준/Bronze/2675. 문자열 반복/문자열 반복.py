t = int(input())

for _ in range(t) :
    r, s = input().split()
    for i in list(s) :
        print(i*int(r), end= '')
    print()