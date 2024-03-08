name = ''
surnames =  []

while name.lower() != 'ok':
    name = input('Enter a surname (ok ends): ')

    if name.lower() != 'ok':
        surnames.append(name)

print()

surnames = list(set(surnames))
surnames.sort()
print(*surnames, sep = ', ')