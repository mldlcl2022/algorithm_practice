# 단어 입력
w = input()

# 알파벳 고윳값 저장
a_list = [i for i in list(set(w.upper()))]

# 각 알파벳의 갯수 저장
n_list = [w.upper().count(i) for i in list(set(w.upper()))]

# 단어에서 가장 많이 사용된 알파벳 출력
if n_list.count(max(n_list))==1 :
    print(a_list[n_list.index(max(n_list))])
else : print('?')