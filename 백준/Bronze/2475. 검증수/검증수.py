n = list(map(int, input().split()))
print(sum([num**2 for num in n])%10)