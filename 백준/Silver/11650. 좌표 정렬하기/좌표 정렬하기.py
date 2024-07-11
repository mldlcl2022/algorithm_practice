n = int(input())
spot = []
for _ in range(n) :
    spot.append(list(map(int, input().split())))
for s in sorted(spot) : print(s[0], s[1])