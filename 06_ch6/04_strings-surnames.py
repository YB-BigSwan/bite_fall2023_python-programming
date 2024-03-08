num = int(input('How many surnames? '))
surnames = []

for i in range(num):
    surname = input('Enter a surname: ')
    fixed_name = surname.capitalize()
    surnames.append(fixed_name)

print()
print(*sorted(set(surnames)), sep = ' ')