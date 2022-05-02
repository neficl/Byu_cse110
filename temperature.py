#Néfi Leite - Byu Pathway

from calendar import c
import math
from string import digits
from unicodedata import digit

def conversion_temperature(value):
    new_value_T = value * 9/5 + 32
    return new_value_T
    
def conversion_windchill(new_value, mph):
    windchill = (35.74 + 0.6215 * new_value - 35.75 * (mph**0.16) + 0.4275 * new_value * (mph ** 0.16))
    #windchill = round(windchill, 2)
    return windchill

score_temperature = float(input("What is the temperature? "))
temperature = input("Fahrenheit or Celsius (F/C)? ")

if temperature.lower() == "c":
    new_value_T = conversion_temperature(score_temperature)
else:
    new_value_T = score_temperature

windSpeed = [5,10,15,20,25,30,35,40,45,50,55,60]
for mph in windSpeed:
    windchill = conversion_windchill(new_value_T, mph)
    print(f"At temperature {new_value_T}F, and wind speed {mph} mph, the windchill is: {windchill: .2f}F")
    
    
    
  