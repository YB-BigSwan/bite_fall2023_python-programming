def main(): 
    team_dictionary = {'John': 'software developer', 'Ann': 'project manager', 'Susan': 'software developer', 'Jill': 'lead developer'}

    for name, role in team_dictionary.items():
        print(f'{name}', end=' ')

    print()
    sorted_keys = list(sorted(team_dictionary.keys()))

    for i in range(len(sorted_keys)):
        print(sorted_keys[i], end=' ')

if __name__ == "__main__":
    main()
