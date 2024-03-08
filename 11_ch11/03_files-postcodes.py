from pathlib import Path

def main():
    file_name = input('Enter postcode file name: ')

    try:
        post_data = load_file(file_name)

        if post_data is not None:
            print(f'{len(post_data)} rows')
            print()
            postcode = input('Enter postcode: ')
            
            if postcode in post_data:
                print(f'{postcode} {post_data[postcode]["Finnish"]}')
                print(f'{postcode} {post_data[postcode]["Swedish"]}')
            else: 
                print('Unknown postcode')

    except FileNotFoundError:
        print()
        print(f'The file {file_name} is not found')

def load_file(file_name):
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

            post_data[postcode] = {'Finnish': finnish_name, 'Swedish': swedish_name}

        return post_data
    
    except FileNotFoundError:
        print()
        print(f'The file {file_name} is not found')
        return None

if __name__ == '__main__':
    main()

