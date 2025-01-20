t = int(input())
for _ in range(t) :
    m,q = input().split()
    s = list(input().split())
    for a in s :
        if q == 'C' : print(ord(a)-64, end= ' ')
        elif q == 'N' : print(chr(int(a)+64), end= ' ')
    print()