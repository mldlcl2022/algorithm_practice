# 색종이 수 입력
n = int(input())

# 도화지 초기 설정
paper = [[0] * 100 for _ in range(100)]

# 색종이 수만큼 반복
for _ in range(n) :
  # 좌표 입력
  x, y = map(int, input().split())
  # x 좌표만큼 반복
  for i in range(x,x+10) :
    # y 좌표만큼 반복
    for j in range(y,y+10) :
      # 해당 범위 값 0을 1로 변경
      paper[i][j] = 1

# 면적 계산을 위한 변수 선언
result = 0
# 도화지 반복
for i in paper :
  # 1 갯수를 세어 면적 계산
  result += i.count(1)
# 결과 출력
print(result)