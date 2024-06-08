s = input()
l = list(s)
t = 0
for i in range(len(l)) :
    if l[i] in 'ABC' : t += 3
    elif l[i] in 'DEF' : t += 4
    elif l[i] in 'GHI' : t += 5
    elif l[i] in 'JKL' : t += 6
    elif l[i] in 'MNO' : t += 7
    elif l[i] in 'PQRS' : t += 8
    elif l[i] in 'TUV' : t += 9
    elif l[i] in 'WXYZ' : t += 10
    else : t += 11
print(t)