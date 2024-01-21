t = int(input())

for _ in range(t) :
    k = int(input()) # 층
    n = int(input()) # 호

    a = [i for i in range(1,n+1)]
    for i in range(k) :
        b = []
        for j in range(n) :
            b.append(sum(a[:j+1]))
        a = b.copy()
    print(a[-1])