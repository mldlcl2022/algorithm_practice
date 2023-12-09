 # 각 말의 개수 입력
c = [int(i) for i in input().split()]

# 체스 말의 개수
chess = [1, 1, 2, 2, 2, 8]

# 말 개수 계산
for n in [chess[i] - c[i] for i in range(6)] : print(n, end = ' ')