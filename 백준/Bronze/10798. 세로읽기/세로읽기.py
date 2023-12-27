# 빈 행렬 생성
l = []
# 행렬 값 입력
for _ in range(5) :
    l.append(list(input()))
# 각각의 배열은 최대 15개 글자로 이루어져 있으므로 15번 반복
for i in range(15) :
    # 1차원 배열은 총 5개로 5번 반복
    for j in range(5) :
        # 순서대로 출력
        try :
            print(l[j][i], end= '')
        except :
            pass