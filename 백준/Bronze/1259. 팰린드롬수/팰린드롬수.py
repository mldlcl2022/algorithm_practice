while True :
    l = list(input())

    if int(l[0]) == 0 : break

    if l == l[::-1] : print('yes')
    else : print('no')