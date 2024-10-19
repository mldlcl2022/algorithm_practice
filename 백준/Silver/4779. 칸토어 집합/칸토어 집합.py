import sys;input = sys.stdin.readline
def recursion(n) :
    if n == 0 : return '-'
    return recursion(n-1) + ' '*(3**(n-1)) + recursion(n-1)

while True :
    try :
        n = int(input())
        print(recursion(n))
    except : break