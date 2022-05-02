child = float(input("What is the price of a child'" + 's' + ' meal? '))
adult = float(input("What is the price of an adult'" + 's' + ' meal? '))
child_Q = int(input('How  many children are there? '))
adult_Q = int(input('How  many adults are there? '))
tax = float(input('What is the sales tax rate? '))
print()

subtotal = (child * child_Q) + (adult*adult_Q)
print(f'Subtotal: ${subtotal:.2f}')
# print(f'Subtotal: ${child*child_Q + adult*adult_Q:.2f}')

sales_tax = (subtotal * tax) / 100
print(f'Sales Tax: ${sales_tax:.2f}')
# print(f'Sales Tax: ${subtotal * tax / 100:.2f}')

total = subtotal + sales_tax
print(f'Total: ${subtotal + sales_tax:.2f}\n')

payment = float(input('What is the payment amount? '))
print(f'Change: ${payment - total:.2f}')
