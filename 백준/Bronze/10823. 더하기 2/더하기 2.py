result = ''
while True :
    try : result += input()
    except : break
print(sum(list(map(int,result.split(',')))))