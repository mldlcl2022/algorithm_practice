# 테스트 케이스의 개수 t 입력
t = int(input())

# 테스트 케이스만큼 반복
for _ in range(t) :
    # 반복 횟수 r, 반복할 문자열 s 입력
    r, s = input().split()
    # 반복한 새로운 문자열 출력
    print(''.join([i*int(r) for i in s[:20]]))