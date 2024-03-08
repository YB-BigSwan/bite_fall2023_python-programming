def main():
    vocabulary = {"cat": "kissa", "dog": "koira", "bird": "lintu"}
    print(vocabulary)

    transpose_dictionary(vocabulary)
    print(vocabulary)

def transpose_dictionary(vocabulary):
    flipped_vocabulary = {}

    for eng_word, fin_word in vocabulary.items():
        flipped_vocabulary[fin_word] = eng_word
    
    vocabulary.clear()
    vocabulary.update(flipped_vocabulary)



if __name__ == '__main__':
    main()