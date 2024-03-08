grades = ["A", "A", "B", "A", "C", "B", "C", "F", "B", "B", "A", "A", "C", "C", "C"]

grade = input('Enter grade letter: ')
count = 0

for i in range(len(grades)):
    if grade.lower() == grades[i].lower():
        count += 1
    
percent = (count / len(grades)) * 100

print(f'{percent:.1f} %')