t = int(input())
coin_list = [0.25, 0.1, 0.05, 0.01]
for _ in range(t) :
    money = (int(input()))
    result = list()
    for coin in coin_list :
        result.append(money//(coin*100))
        money %= (coin*100)
    for i in result :
        print(int(i), end= ' ')