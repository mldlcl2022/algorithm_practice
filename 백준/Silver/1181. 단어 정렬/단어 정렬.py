n = int(input())
w_list = {}
for _ in range(n) :
    w = input()
    w_list[w] = len(w)

for w in sorted(list(w_list.items()), key= lambda x: (x[1], x[0])) :
    print(w[0])