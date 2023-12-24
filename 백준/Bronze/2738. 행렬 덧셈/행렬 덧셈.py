# 행렬의 크기 n, m 입력
n, m = map(int, input().split())

# 행렬 계산을 위한 빈 리스트 생성
a, b = [], []

# a 행렬 값 입력
for _ in range(n) :
    a.append(list(map(int, input().split())))

# b 행렬 값 입력
for _ in range(n) :
    b.append(list(map(int, input().split())))
    
# 행렬 합 결과 출력
for i in range(n) :
    for j in range(m) :
        print(a[i][j]+b[i][j], end= ' ')
    print()