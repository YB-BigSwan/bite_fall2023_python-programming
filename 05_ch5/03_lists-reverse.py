int_number = int(input('How many integers? '))
int_list = []

for i in range(int_number):
    num = int(input('Enter an integer: '))
    int_list.append(num)

print()
int_list.reverse()
print(*int_list)