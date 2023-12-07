# 총 바구니 수 n, 공을 넣을 횟수 m 입력
n, m = map(int, input().split())

# 초기 바구니 설정
b = [0 for _ in range(n)]

# 공을 넣을 횟수만큼 반복
for _ in range(m) :
    # 시작 바구니 i, 마지막 바구니 j, 넣을 공의 번호 k 입력
    i, j, k = map(int, input().split())
    # 시작 바구니부터 마지막 바구니까지 k번 공 넣기
    for l in range(i, j+1) :
        b[l-1] = k

# 1번 바구니부터 n번 바구니까지 들어있는 공의 번호 출력
for i in range(n) :
    print(b[i], end= ' ')