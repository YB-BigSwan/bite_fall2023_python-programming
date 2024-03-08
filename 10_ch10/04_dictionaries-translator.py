def main():
    dictionary = {}

    eng_input = ''
    dict_input = ''

    print('=== Creating a dictionary ===')

    while eng_input !=  'quit':
        eng_input = input('Enter english word (quit ends): ').lower()
        
        if eng_input != 'quit':
            fin_input = input('Enter finnish word: ').lower()
            dictionary[eng_input] = fin_input

    print('\n=== Using a dictionary ===')
    while dict_input != 'quit':
        dict_input = input('Enter english word (quit ends): ').lower()

        if dict_input != 'quit' and dict_input in dictionary:
            print(f'{dictionary[dict_input]}\n')
        elif dict_input != 'quit' and dict_input not in dictionary:
            print('Unknown word\n')

if __name__ == '__main__':
    main()