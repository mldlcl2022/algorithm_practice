n = int(input())
num_list = list(map(int, input().split()))[:n]

result = 0
for num in num_list :
    error = 0
    if num > 1 :
        for i in range(2,num) :
            if num % i == 0 :
                error += 1
        if error == 0 :
            result += 1
print(result)