def main():
    team_dictionary = {'John': 'software developer', 'Ann': 'project manager', 'Susan': 'software developer', 'Jill': 'lead developer'}

    role_list = sorted(set(team_dictionary.values()))

    for role in role_list:
        print(role, end='\n')

if __name__ == '__main__':
    main()