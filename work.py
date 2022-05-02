print('Please to fill informations')
First_name = input('What is your first name: ')
Last_name = input('What is your last name: ')
Email_Address = input('What is your Email Address: ')
Phone_Number = input('Whats is your Phone Number: ')
Job_title = input('What is your Job title: ')
Id_Number = input('What is your ID Number: ')
color_Hair = input('What is color of your Hair: ')
color_Eyes = input('What is color of your Eyes: ')
Month = input('What is Month to your birthday: ')
Answer = input('Are you Training: ')

print("\nThe ID Card is: ")
print("----------------------------------------")
print(Last_name.upper() + ', ' + First_name.capitalize()) 
print(Job_title.title()) 
print("ID: " + Id_Number + '\n')
print(Email_Address.lower()) 
print(Phone_Number + '\n')
print(f"Hair: {color_Hair:11} Eyes:  + {color_Eyes}")
print(f"Month: {Month:9} Training: {Answer}")
print("----------------------------------------\n")
print('Thank you for participating in campaign!')





