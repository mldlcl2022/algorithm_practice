t = int(input())
for _ in range(t) :
    R,S = input().split()
    for s in S :
        print(s*int(R), end= '')
    print()