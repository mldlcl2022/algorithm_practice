l = int(input())
result = 0
for i in range(5,0,-1) :
    if l // i > 0 :
        result += (l//i)
        l = l % i
print(result)