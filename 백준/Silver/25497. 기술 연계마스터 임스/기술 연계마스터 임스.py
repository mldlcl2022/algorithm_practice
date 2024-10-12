import sys;input = sys.stdin.readline
n = int(input())
skill = input().rstrip()

lr = 0
sk = 0
cnt = 0
for command in skill :
    if command not in ['L','R','S','K'] : cnt += 1
    elif command == 'L' : lr += 1
    elif command == 'R' :
        if lr > 0 : lr -= 1;cnt += 1
        else : break
    elif command == 'S' : sk += 1
    elif command == 'K' :
        if sk > 0 : sk -= 1;cnt += 1
        else : break
print(cnt)