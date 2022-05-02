from datetime import datetime

current_date = datetime.now()
print('Today is: ' + str(current_date))

birthday = input('When is your birthday (dd/mm/yyyy)? ')
birthday_date = datetime.strptime(birthday, '%d/%m/%Y')
print('Birthday: ' + str(birthday_date))
