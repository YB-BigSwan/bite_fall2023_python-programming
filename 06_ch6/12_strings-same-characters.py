string1 = input('Enter first string: ').replace(' ', '')
string2 = input('Enter second string: ').replace(' ', '')

sorted_string1 = ''.join(sorted(string1.lower()))
sorted_string2 = ''.join(sorted(string2.lower()))

if sorted_string1 == sorted_string2:
    print('Same characters')
else:
    print('Different characters')