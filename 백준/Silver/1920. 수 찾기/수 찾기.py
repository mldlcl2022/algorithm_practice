import sys;input = sys.stdin.readline
from bisect import bisect_left
n = int(input())
a = list(map(int, input().split()))
m = int(input())
checklist = list(map(int, input().split()))

a.sort()
for num in checklist :
    try :
        if num == a[bisect_left(a,num)] : print(1)
        else : print(0)
    except : print(0)