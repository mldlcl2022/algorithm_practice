n = int(input())

no = 0
d = []
for _ in range(n) :
    age, name = input().split()
    d.append([no, name, int(age)])
    no += 1

for w in sorted(d, key= lambda x: (x[2], x[0])) :
    print(w[2], w[1])