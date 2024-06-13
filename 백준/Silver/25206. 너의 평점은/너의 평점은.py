g_index = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}

d_all = 0
dxg = 0
for _ in range(20) :
    s,d,g = input().split()
    if g == 'P' : pass
    else :
        # 학점의 총합 계산
        d_all += float(d)
        # 학점 x 평점 합 계산
        dxg += (float(d) * g_index[g])
print(dxg/d_all)