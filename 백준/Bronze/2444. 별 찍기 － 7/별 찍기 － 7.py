n = int(input())
for i in range(1,n+1) :
    print(' '*(((2*n-1)-(2*i-1))//2) + '*'*(2*i-1))
for i in range(n-1,0,-1) :
    print(' '*(((2*n-1)-(2*i-1))//2) + '*'*(2*i-1))