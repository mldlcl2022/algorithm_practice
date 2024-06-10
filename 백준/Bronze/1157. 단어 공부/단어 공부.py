s = input()
l = list(set(s.upper()))
n = []
for w in l :
    n.append(s.upper().count(w))
if n.count(max(n)) != 1 : print('?')
else : print(l[n.index(max(n))])