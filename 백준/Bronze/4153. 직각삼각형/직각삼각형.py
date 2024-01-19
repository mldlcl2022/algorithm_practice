while True :
  a, b, c = map(int, input().split())
  if a == b == c == 0 : break
  if (sorted([a, b, c])[0]**2 + sorted([a, b, c])[1]**2) == sorted([a, b, c])[2]**2 : print('right')
  else : print('wrong')