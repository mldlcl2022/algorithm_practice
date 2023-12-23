# 학점 총합 계산을 위한 변수
c_sum = 0
# (학점 X 과목평점)의 합을 계산하기 위한 변수
g_sum = 0
# 20 과목 입력
for _ in range(20) :
    # 과목명, 학점, 성적 입력
    s, c, g = input().split()
    # 성적이 P가 아닌 경우 학점 총합 계산
    if g != 'P' : c_sum += float(c)
    # 괴목평점에 따라 계산
    if g == 'A+' : g_sum += float(c)*4.5
    elif g == 'A0' : g_sum += float(c)*4
    elif g == 'B+' : g_sum += float(c)*3.5
    elif g == 'B0' : g_sum += float(c)*3
    elif g == 'C+' : g_sum += float(c)*2.5
    elif g == 'C0' : g_sum += float(c)*2
    elif g == 'D+' : g_sum += float(c)*1.5
    elif g == 'D0' : g_sum += float(c)*1
    elif g == 'F' : g_sum += float(c)*0
    else : pass
# 평점 결과 출력
print(g_sum/c_sum)