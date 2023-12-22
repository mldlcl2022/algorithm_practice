# 단어 갯수 입력
n = int(input())

# 단어 갯수 계산을 위한 변수 생성
cnt = n

# 단어 갯수만큼 반복
for _ in range(n) :
    # 단어 입력
    word = input()
    # 단어마다 반복
    for i in range(len(word)-1) :
        # 현재 알바펫이 다음 알파벳가 같은 경우 pass
        if word[i] == word[i+1] :
            continue
        # 현재 알파벳이 이후 알파벳 중에 있으면 stop
        elif word[i] in word[i+1:] :
            cnt -= 1
            break

# 단어 갯수 출력
print(cnt)