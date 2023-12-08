# 두 수 a, b 입력
a, b = input().split()

# 상수 기준 큰 수
print(max(int(a[::-1]), int(b[::-1])))