word = input()
print(''.join([w.lower() if w == w.upper() else w.upper() for w in list(word)]))