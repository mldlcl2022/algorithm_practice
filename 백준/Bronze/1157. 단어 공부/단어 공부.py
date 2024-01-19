s = [i.upper() for i in list(input())]

n = []
for w in list(set(s)) :
    n.append(s.count(w))
if n.count(max(n)) > 1 :
    print('?')
else :
    print(list(set(s))[n.index(max(n))])