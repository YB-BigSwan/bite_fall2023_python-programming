from urllib.request import urlopen

url = "https://www.mit.edu/~ecprice/wordlist.10000"
word_list = urlopen(url).read().decode('utf-8').splitlines()

counters = [0] * 23
word_amount = len(word_list)
word_length = 0

for i in range(len(word_list)):
    length = len(word_list[i])
    word_length += length
    if length < len(counters):
        counters[length] += 1

avg_length = word_length/word_amount

print(f'{word_amount} words')
print(f'The average word length is {avg_length}')
print(f"{'Length':>6s}{'Count':>6s}")
for i in range(1, len(counters)):
    print(f"{i:>6d}{counters[i]:>6d}")
