from urllib.request import urlopen

def main():
    url = "https://www.mit.edu/~ecprice/wordlist.10000"
    content = urlopen(url).read().decode("UTF-8")

    letter_count = {}

    for letter in content:
        if letter.isalpha():
            sanitized_letter = letter.lower()
            letter_count[sanitized_letter] = letter_count.get(sanitized_letter, 0) +1

    sorted_letters = sorted(letter_count.items())

    for letter, count in sorted_letters:
        print(f'{letter}: {count}')



if __name__ == '__main__':
    main()



