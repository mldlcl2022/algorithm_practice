t = int(input())
for _ in range(t) :
    H,W,N = map(int, input().split())
    floor = N%H
    line = (N//H)+1
    if floor == 0 :
        floor = H
        line -= 1
    print(floor*100+line)