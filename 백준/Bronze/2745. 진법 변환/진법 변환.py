n, b = input().split()
arr = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n = n[::-1]
b = int(b)
result = 0
for i in range(len(n)-1,-1,-1) :
  result += arr.index(n[i])*(b**i)
print(result)