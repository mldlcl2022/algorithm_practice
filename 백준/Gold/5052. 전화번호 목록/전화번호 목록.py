import sys;input = sys.stdin.readline
t = int(input())
for _ in range(t) :
    n = int(input())
    tel_list = []
    for _ in range(n) :
        tel_list.append(input().rstrip())
    
    tel_list.sort()
    result = 'YES'
    for i in range(1,len(tel_list)) :
        if tel_list[i].startswith(tel_list[i-1]) : result = 'NO'
        else : continue
    print(result)