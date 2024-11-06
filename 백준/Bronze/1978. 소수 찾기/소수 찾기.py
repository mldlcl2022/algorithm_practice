n = int(input())
nums = list(set(map(int, input().split())))

cnt = 0
for num in nums :
    tmp = 0
    if num > 1 :
        for i in range(2,num) :
            if num % i == 0 :
                tmp += 1
                break
        if tmp == 0 : cnt += 1
print(cnt)