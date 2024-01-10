t = int(input())
for _ in range(t) :
  ox = input()
  n = 1
  result = 0
  for s in ox :
    if s == 'O' :
      result += n
      n += 1
    elif s == 'X' :
      n = 1
  print(result)