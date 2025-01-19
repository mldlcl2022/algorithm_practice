n = int(input())
word = input()
h,i,a,r,c = 0,0,0,0,0
for s in list(word):
    s = s.lower()
    if s == 'h' : h += 1
    elif s == 'i' : i += 1
    elif s == 'a' : a += 1
    elif s == 'r' : r += 1
    elif s == 'c' : c += 1
print(min(h,i,a,r,c))