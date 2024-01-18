l = int(input())
s = input()[:l]
a = [ord(i)-96 for i in list(s)]

result = 0
for i in range(len(a)) :
    result += a[i]*(31**i)
print(result) 