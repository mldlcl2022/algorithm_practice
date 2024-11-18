n = int(input())
words = {}
for _ in range(n) :
    word = input()
    words[word] = len(word)

for word in sorted(list(words.items()), key= lambda x: (x[1], x[0])) :
    print(word[0])