# 과제 제출 확인을 위한 리스트 선언
s = []

# 과제 제출 학생 기록
for i in range(28) : s.append(int(input()))

# 과제 미제출자 출력
for i in sorted([i for i in range(1,31,1) if i not in s]) : print(i)