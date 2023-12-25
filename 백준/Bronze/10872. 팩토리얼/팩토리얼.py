# 정수 n 입력
n = int(input())
# 계산을 위한 변수 생성
result = 1
# n 팩토리얼 계산
for i in range(1,n+1) :
    result *= i
# 결과 출력
print(result)