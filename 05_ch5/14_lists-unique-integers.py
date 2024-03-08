int_list = []

for i in range(5):
    num = int(input('Enter an integer: '))
    int_list.append(num)

print(*sorted(set(int_list)), sep = ', ')
print(*sorted(int_list), sep = ', ')
    