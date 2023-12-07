# 총 바구니 수 n, 공을 바꿀 횟수 m 입력
n, m = map(int, input().split())

# 초기 바구니 설정
b = [i+1 for i in range(n)]

# 임시 변수
temp = 0

# 공을 바꿀 횟수만큼 반복
for _ in range(m) :
    # 바꿀 바구니 번호 1, 바꿀 바구니 번호 2
    i, j = map(int, input().split())
    # 임시 변수에 첫 번째 바구니 값 임시 저장
    temp = b[i-1]
    # 첫 번째 바구니 값을 두 번째 바구니 값으로 변경
    b[i-1] = b[j-1]
    # 두 번째 바구니 값을 임시 저장한 첫 번째 바구니 값으로 변경
    b[j-1] = temp

# 결과 확인
for num in b :
    print(num, end = ' ')