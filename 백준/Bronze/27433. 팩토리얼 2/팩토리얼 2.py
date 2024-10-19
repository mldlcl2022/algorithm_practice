import sys;input = sys.stdin.readline
def factorial(num):
    if num <= 1 : ans = 1
    else : ans = factorial(num-1) * num
    return ans

n = int(input())
print(factorial(n))