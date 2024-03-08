from pathlib import Path

def main():
    file_name = 'postcodes.csv'

    try:
        post_data = load_data(file_name)

        if post_data is not None:
            user_input = input('Enter place name: ')
            sanitized_input = user_input.upper()
            found = False
            
            for postcode, name in post_data.items():
                if sanitized_input in [name["Finnish"], name["Swedish"]]:
                    if sanitized_input == name["Finnish"]:
                        print(f'{postcode} {name["Finnish"]}')
                        found = True
                    elif sanitized_input== name["Swedish"]:
                        print(f'{postcode} {name["Swedish"]}')
                        found = True

            if not found:
                print(f'\nNo postoffice found')
            

    except FileNotFoundError:
        print()
        print(f'The file {file_name} is not found')

def load_data(file_name):
    path = Path(__file__).resolve().parent
    path = path / file_name

    try:
        content = path.read_text(encoding='UTF-8')
        lines = content.splitlines()

        post_data = {}
        for line in lines:
            values = line.split(';')
            postcode = values[0]
            finnish_name = values[1]
            swedish_name = values[2]

            post_data[postcode] = {'Postcode': postcode, 'Finnish': finnish_name, 'Swedish': swedish_name}

        return post_data
    
    except FileNotFoundError:
        print()
        print(f'The file {file_name} is not found')
        return None

if __name__ == '__main__':
    main()

