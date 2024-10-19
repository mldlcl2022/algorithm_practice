import sys;input = sys.stdin.readline

def fibonacci(num) :
    if num <= 1 : ans = num
    else : ans = fibonacci(num-1) + fibonacci(num-2)
    return ans

n = int(input())
print(fibonacci(n))