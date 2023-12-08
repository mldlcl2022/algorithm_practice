# 단어 s 입력
s = input()

# 알파벳 전체 반복
for i in [chr(j) for j in range(97,123)] :
    # 알파벳이 입력한 단어 s에 있다면 위치 출력
    try : print(s.index(i), end = ' ')
    # 알파벳이 입력한 단어 s에 없다면 -1 출력
    except : print(-1, end = ' ')