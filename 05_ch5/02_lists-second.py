words = []
word = ''

while word != 'quit':
    word = input('Enter a word (quit ends): ')
    if word.lower() != 'quit':
        words.append(word)

words.sort()
print(*words, sep = '\n')