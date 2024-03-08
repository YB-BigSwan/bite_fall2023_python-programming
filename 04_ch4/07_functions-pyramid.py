def print_pyramid(pyramid_height):
        for i in range(1, pyramid_height + 1):
            print((' ' * (pyramid_height - i)) + ('*' * (2 * i - 1)))

def main():
    pyramid_height = int(input('Enter pyramid height: '))
    print_pyramid(pyramid_height)

if __name__ == "__main__":
    main()