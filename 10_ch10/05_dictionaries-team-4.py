def main():
    team_dictionary = {'John': 'software developer', 'Ann': 'project manager', 'Susan': 'software developer', 'Jill': 'lead developer'}

    name = ''
    role = ''

    while name.lower() !=  'quit':
        name = input('Enter name (quit ends): ')
        
        if name.lower() != 'quit':
            role = input('Enter role: ')
            team_dictionary[name] = role
            print()

    print()
    for name, role in sorted(team_dictionary.items()):
        print(f'{name:8s}{role:8s}')

if __name__ == '__main__':
    main()