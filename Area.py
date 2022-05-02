import math
pi = float(math.pi)

square = float(input('What is the length of a side of the square? '))
print(f'The area of the square is: {square*square:.1f}')
lenght_R = float(input('What is the length of rectangle? '))
width_R = float(input('What is the width of the rectangle? '))
print(f'The area of the rectangle is: {lenght_R*width_R:.1f}')

radius = float(input('What is the radius of the circle? '))
print(f'The area of the circle is: {pi * (radius * radius):.1f}')


