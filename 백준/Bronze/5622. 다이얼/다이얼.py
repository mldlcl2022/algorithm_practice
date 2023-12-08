# 단어 s 입력
s = input()

# 시간 계산을 위한 리스트 생성
l = []

# 단어 s의 글자마다 반복
for i in s :
    # 글자가 ABC 중 하나면 2 + 1(1초씩 더 걸리기 때문)
    if i in 'ABC' : l.append(2+1)
    # 글자가 DEF 중 하나면 3 + 1
    elif i in 'DEF' : l.append(3+1)
    # 글자가 GHI 중 하나면 4 + 1
    elif i in 'GHI' : l.append(4+1)
    # 글자가 JKL 중 하나면 5 + 1
    elif i in 'JKL' : l.append(5+1)
    # 글자가 MNO 중 하나면 6 + 1
    elif i in 'MNO' : l.append(6+1)
    # 글자가 PQRS 중 하나면 7 + 1
    elif i in 'PQRS' : l.append(7+1)
    # 글자가 TUV 중 하나면 8 + 1
    elif i in 'TUV' : l.append(8+1)
    # 글자가 WXYZ 중 하나면 9 + 1
    elif i in 'WXYZ' : l.append(9+1)

# 최소 시간 출력
print(sum(l))