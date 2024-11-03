a = int(input())
b = int(input())
c = int(input())
num = a*b*c
for i in range(10) :
    print(list(map(int, list(str(num)))).count(i))