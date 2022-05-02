old = int(input('How old are you? '))
age = old + 1
print('On your next birthday, you will be ' + str(age))
print(f'On your next birthday, you will be {old + 1}.')
print()

eggs = int(input('How  many egg cartons do you have? '))
cartons = 12 * eggs
print(f'You have {cartons} eggs')
print(f'You have {eggs * 12} eggs')
print()

cookies = float(input('How many cookies do you have? '))
people = float(input('How many people are there? '))
total = cookies / people
print('Each person may have ' + str(total) + ' cookies')
print(f'Each person may have {cookies/people:.2f} cookies')
print(f'Each person may have {cookies/people:.0%} cookies')