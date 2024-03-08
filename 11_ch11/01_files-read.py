from pathlib import Path

def main():
    file_name = input('Enter file name: ')
    path = Path(file_name)
    
    try:
        content = path.read_text(encoding='UTF-8')
        print(content)
    except FileNotFoundError:
        print()
        print(f'The file {file_name} is not found')
    
   

if __name__ == '__main__':
    main()

