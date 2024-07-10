n = int(input())
size = list(map(int, input().split()))
t,p = map(int, input().split())

num_t = 0
for s in size :
    if (s!=0)&(s<=t) : num_t += 1
    elif (s!=0)&(s>t) :
        if (s%t) == 0 : num_t += (s//t)
        else : num_t += ((s//t)+1)
print(num_t)
print(n//p, n%p)