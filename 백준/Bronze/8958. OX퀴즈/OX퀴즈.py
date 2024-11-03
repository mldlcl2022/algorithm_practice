t = int(input())
for _ in range(t) :
    ox = input()
    tmp = 0
    score = 0
    for i in range(len(ox)) :
        if i == 0 :
            if ox[i] == 'O' :
                tmp += 1
                score += tmp
        else :
            if ox[i] == 'O' :
                tmp += 1
                score += tmp
            else : tmp = 0
    print(score)