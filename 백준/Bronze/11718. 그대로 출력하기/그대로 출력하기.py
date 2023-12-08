# 무한 루프
while True :
    # 입력한 단어가 있다면 출력
    try : print(input())
    # 입력한 단어가 없다면 종료
    except EOFError : break