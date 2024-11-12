l = []
for i in range(3) :
    s = input()
    try : l.append((int(s), i))
    except : l.append((s,i))

num = 0
for i in range(-1,-4,-1) :
    if type(l[i][0]) == int :
        if l[i][1] == 2 : num += (l[i][0]+1)
        elif l[i][1] == 1 : num += (l[i][0]+2)
        else : num += (l[i][0]+3)
    if num != 0 : break

if num % 3 == 0 and num % 5 == 0 : print('FizzBuzz')
elif num % 3 == 0 and num % 5 != 0 : print('Fizz')
elif num % 3 != 0 and num % 5 == 0 : print('Buzz')
else : print(num)