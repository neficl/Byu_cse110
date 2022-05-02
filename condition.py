x = 5
y = 10

if x == 5:
    print("a")

    if y == 6:
        print("b")
else:
    print("c")

    if y == 10:
        print("d")
        
gpa=float(input("Whats is your GPA?\n"))

lowest_grade = 60;
          
if gpa >= 80:
    if lowest_grade >= 70:
        print('Well Done')
    elif lowest_grade == 60:
        print('Hello')
    else:
        honour_roll=False
        print('Error')

if gpa >= 85 or lowest_grade >= 70:
    print('Well Done')
    

#if province in('Alberta', 'Nunavut', 'Yukon'):
