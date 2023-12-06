# library
import sys

# enter n
n = int(input())

# result
for i in range(n) :
    # enter a, b
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)