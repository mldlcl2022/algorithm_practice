l = int(input())
s = input()
r = 31
m = 1234567891

result = 0
for i in range(l) :
    result += (ord(s[i])-96) * (31**i)
print(result%m)