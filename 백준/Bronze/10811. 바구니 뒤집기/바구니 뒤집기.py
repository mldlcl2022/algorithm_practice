# 총 바구니 수 n, 공을 바꿀 횟수 m 입력
n, m = map(int, input().split())

# 초기 바구니 설정
b = [i+1 for i in range(n)]

# 임시 변수
temp = []

# 공을 바꿀 횟수만큼 반복
for _ in range(m) :
    # 바꿀 첫 번째 바구니 i, 마지막 바구니 j
    i, j = map(int, input().split())
    # i ~ j 번째 숫자 임시 저장
    temp = b[i-1:j]
    # i ~ j 번째 숫자 역순 변환
    b[i-1:j] = temp[::-1]

# 결과 출력
for i in b : print(i, end = ' ')