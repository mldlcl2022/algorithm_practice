# 빈 행렬 생성
m = []
# 행렬 값 입력
for _ in range(9) :
    m.append(list(map(int, input().split())))
# 최댓값 결과 출력
print(max([max(i) for i in m]))
# 최댓값 계산을 위한 변수 생성
max_value = 0
# 행, 열 변수 생성
row = 0
col = 0
# 열만큼 반복
for i in range(len(m)) :
    # 행만큼 반복
    for j in range(len(m[i])) :
        # 최댓값 계산
        if m[i][j] > max_value :
            max_value = m[i][j]
            # 최댓값의 행, 열 저장
            row = i
            col = j
        else : continue
# 최댓값의 행, 열 결과 출력
print(row+1, col+1)