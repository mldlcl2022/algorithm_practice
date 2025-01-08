s = [i for i in range(1,31)]
for _ in range(28) :
    num = int(input())
    s.remove(num)
for i in sorted(s) :
    print(i)