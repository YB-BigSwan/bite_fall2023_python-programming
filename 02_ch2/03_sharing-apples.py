appleCount = int(input('How many apples? '))
childCount = int(input('How many children? '))

apc= appleCount // childCount
leftovers= appleCount % childCount

print(f'\nEach child will get {apc} apples.')
print(f'There will be {leftovers} leftover apples.')