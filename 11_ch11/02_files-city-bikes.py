from pathlib import Path

def main():
    file_name = input('Enter file name: ')

    try:
        ride_data = load_file(file_name)

        if ride_data is not None:
            print()
            show_statistics(ride_data)

    except FileNotFoundError:
        print()
        print(f'The file {file_name} is not found')

def load_file(file_name):
    path = Path(__file__).resolve().parent
    path = path / file_name

    try:
        content = path.read_text(encoding='UTF-8')
        lines = content.splitlines()
        return lines[1:]
    
    except FileNotFoundError:
        print()
        print(f'The file {file_name} is not found')
        return None
    
   
def show_statistics(ride_data):
    total_distance = 0
    total_duration = 0
    total_rides = len(ride_data)

    for line in ride_data:
        _, _, _, _, _, _, distance, duration = line.split(',')
        total_distance += float(distance)
        total_duration += int(duration)


    convert_distance = total_distance / 1000
    average_distance = (total_distance / total_rides) / 1000
    average_duration = (total_duration / total_rides) / 60

    print(f'{convert_distance:.0f} kilometers on {total_rides} bike rides')
    print(f'Average distance: {average_distance:.1f} kilometers')
    print(f'Average duration: {average_duration:.0f} minutes')


if __name__ == '__main__':
    main()

