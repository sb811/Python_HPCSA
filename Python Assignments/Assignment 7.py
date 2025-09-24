'''

Assignment 1: Temperature convertor

Input from user :

    Temperature value and unit
    Temperature unit to convert to


Functions :

    • celsius_to_fahrenheit(celsius)
    • fahrenheit_to_celsius(fahrenheit)
    • celsius_to_kelvin(celsius)

Employ exception handling for checking numeric values.
Implement Finally block


'''


for i in range(3):
    try:
        temp = int(input("Enter the Temperature in Number: "))
        break
    except ValueError:
        print("Error: Please enter a numeric value. You have a few more tries.")
else:
    print("You have exceeded the maximum number of attempts.")
    exit()

temp_unit = input("Enter the Unit (C/F/K): ").lower()
unit_to_convert = input("Enter the Unit (C/F/K): ").lower()

def celsius_to_fahrenheit():
    celsius = temp
    fahrenheit = 0
    fahrenheit = (celsius * 9/5) + 32
    print(f'Celsius to Fahrenheit :  {celsius}C == {fahrenheit}F')


def fahrenheit_to_celsius():
    fahrenheit = temp
    celsius = 0
    celsius = (fahrenheit - 32) * 5/9
    print(f'Fahrenheit to Celsius :  {fahrenheit}F == {celsius}C')

def celsius_to_kelvin():
    celsius = temp
    kelvin = 0
    kelvin = celsius + 273.15
    print(f'Celsius to Kelvin :  {celsius}C == {kelvin}K')


if unit_to_convert == "f":
    celsius_to_fahrenheit()
elif unit_to_convert == "c":
    fahrenheit_to_celsius()
elif unit_to_convert == "k":
    celsius_to_kelvin()
else:
    print("Invalid Input")