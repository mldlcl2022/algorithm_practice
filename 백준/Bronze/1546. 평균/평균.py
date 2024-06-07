n = int(input())
l = list(map(int,input().split()))[:n]
m = max(l)
print(sum([i/m*100 for i in l])/n)