def main():
    team_dictionary = {'John': 'software developer', 'Ann': 'project manager', 'Susan': 'software developer', 'Jill': 'lead developer'}

    name = ''

    while name.lower() != 'quit':
        name = input('Enter name (quit ends): ')

        if name.lower() != 'quit' and name in team_dictionary:
            print(f'{name} is a {team_dictionary[name]}')
        elif name.lower() != 'quit': 
            print(f'{name} is not in the team')

if __name__ == "__main__":
    main()