import sys;input = sys.stdin.readline
t = int(input())
for _ in range(t) :
    n = int(input())
    grade = []
    for _ in range(n) :
        p,i = map(int, input().split())
        grade.append((p,i))
    grade.sort(key= lambda x: (x[0],x[1]))
    
    cnt = 1
    current = grade[0][1]
    for i in range(1,n) :
        if grade[i][1] < current :
            current = grade[i][1]
            cnt += 1
    print(cnt)