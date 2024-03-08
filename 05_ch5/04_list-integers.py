nums = []
for i in range(5):
    num = int(input('Enter an integer: '))
    nums.append(num)

print()

nums.sort(reverse = True)

for i in range(len(nums)):
    print(nums[i], end = ' ')