# 테스트 케이스의 개수 t 입력
t = int(input())

# 테스트 케이스만큼 반복
for _ in range(t) :
    # 문자열 입력
    s = input()
    # 문자열의 첫 글자와 마지막 글자 출력
    print(s[0]+s[-1])