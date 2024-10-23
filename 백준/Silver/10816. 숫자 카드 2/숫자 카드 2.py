import sys;input = sys.stdin.readline
n = int(input())
cards = list(map(int, input().split()))
m = int(input())
checklist = list(map(int, input().split()))

d = {}
for num in cards :
    if num in d : d[num] += 1
    else : d[num] = 1
for num in checklist :
    if num in d : print(d[num], end= ' ')
    else : print(0, end= ' ')