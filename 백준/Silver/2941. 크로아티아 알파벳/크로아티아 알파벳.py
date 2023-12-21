# 단어 입력
w = input()

# 크로아티아 알파벳 리스트
c_a = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

# 크로아티아 알파벳이 있는 경우 특정문자('a')로 변경
for a in c_a :
    w = w.replace(a,'a')

# 크로아티아 알파벳 갯수 출력
print(len(w))