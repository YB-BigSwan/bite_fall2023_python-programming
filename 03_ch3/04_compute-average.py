number = float(input("Enter first number: "))
count = 0
sum = 0
        

while number != 0:
    sum += number
    count += 1
    number = float(input('Enter next number: '))



if count == 0:
    print('Nothing to be calculated')
else:
    average = sum/count
    print(f'The average is {average:.2f}')
