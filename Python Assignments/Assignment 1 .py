# Assignment 1: Swap values of 2 variables

var1 = 2
var2 = 5
print (f'The Numbers Before swapping var1 : {var1} & var2 : {var2}')

var2, var1 = var1, var2
print (f'The Numbers After swapping var1 : {var1} & var2 : {var2}')

# Assignment 2: Try out Arithmetic and Assignment operators

var1 = int(input("Enter 1 no: "))
var2 = int(input("Enter 2 no: "))
var3 = 100

# Arithmatic Operators

# 1. Addition Operation
print ("The Sum is", var1 + var2)

# 2. Substraction Operation
print ("The Difference is", var1 - var2)

# 3. Multiplication Operation
print ("The Multiplication is", var1 * var2)

# 4. Division Operation
print ("The Division is", var1 / var2)

# 5. Mod Operation
print ("The Mod is", var1 % var2)

# 6 Power Operation
print ("The Power is", var1 ** var2)


# Assignment Operartors

# 1. Start with an initial score
print(f"Initial score: {var3}")

# 2. Add 50
var3 += 50
print(f"After adding 50: {var3}")

# 3. Subtract 25
var3 -= 25
print(f"After subtracting 25: {var3}")

# 4. Multiply by 2
var3 *= 2
print(f"After multiplying by 2: {var3}")

# 5. Divide by 10
var3 /= 10
print(f"Final score: {var3}")


# Assignment 3: Implement comparison operators 

num1 = int(input("Enter 1 no: "))
num2 = int(input("Enter 2 no: "))


# Equality check
is_equal = (num1 == num2)
print(f"Is num1 equal to num2? {is_equal}")

# Not equal check
is_not_equal = (num1 != num2)
print(f"Is num1 not equal to num2? {is_not_equal}")

# Greater than check
is_greater = (num1 > num2)
print(f"Is num1 greater than num2? {is_greater}")

# Less than check
is_less = (num1 < num2)
print(f"Is num1 less than num2? {is_less}")

# Greater than or equal to check
is_greater_or_equal = (num1 >= num2)
print(f"Is num1 greater than or equal to num2? {is_greater_or_equal}")

# Less than or equal to check
is_less_or_equal = (num1 <= num2)
print(f"Is num1 less than or equal to num2? {is_less_or_equal}")

# Declare two string variables
str1 = str(input("Enter 1 String: ")) 
str2 = str(input("Enter 2 String: "))

# Equality check
are_strings_equal = (str1 == str2)
print(f"Are str1 and str2 equal? {are_strings_equal}")

# Not equal check
are_strings_not_equal = (str1 != str2)
print(f"Are str1 and str2 not equal? {are_strings_not_equal}")



# Assignment 4: Build a calculator for +, -, * and / operations using if and else condition statements

var1 = int(input("Enter 1 no: "))
var2 = int(input("Enter 2 no: "))

# Choose Operation to be perform
operand = input("Enter the Operand (+,-,*,/): ")

if (operand == "+"):
    print(f'The sum is : {var1+var2}')
elif (operand == "-"):
    print(f'The Difference is : {var1-var2}')
elif (operand == "*"):
    print(f'The product is : {var1*var2}')
elif (operand == "/"):
    print(f'The division is : {var1/var2}')


# Assignment 5: Accept 2 numbers from user add them, print them. 

num1 = int(input("Enter 1 no: "))
num2 = int(input("Enter 2 no: "))

print ("Addition is: ", num1 + num2)


#Assignment 6: Add an integer and a float, print result and type of result

num1 = int(input("Enter Integer: "))
num2 = float(input("Enter Float: "))

print ("The Result is" , num1 + num2)

# Assignment 7: Accept a float value from console typecast it to float and print its square
num = float(input("Enter Float: "))
print ("Square of no is: ", num ** 2)


# Assignment 8: Add a string and a number, print result and type of result

string = input("Enter a String: ")
num = input("Enter a no: ")
print ("Adding String and No: ", string+num)


# Assignment 9: Build a program that calculates the ticket price based on the age of the customer.
''' Input: Prompt the user to enter their age.
Logic:
• Use if-else statements to determine the ticket price based on age:
• Under 5 years: Free
• 5 to 12 years: Rs 5
• 13 to 60 years: Rs 10
• Over 60 years: Rs 7
• Use nested if-else statements if necessary for more granular control.
Output: Display the ticket price based on the user's age
'''

age = int(input("Please Enter your Age: "))

if age<5:
    print ("Ticket is Free")
elif age>=5 and age<=12:
    print ("Ticket is Rs 5.")
elif age>=13 and age<=30:
    print ("Ticket is Rs 10.")
elif age>=60:
    print ("Ticket is Rs 7.")


# Class Questions: 1
# WAP that will take number as a input and add that number to recent previous number is divisible by '5' then print result

num=int(input("Please Enter a Number: ")) 
num2=num%5
if num2!=0:
    print(num-num2+num)
else:
    print(num+num-5)


# Class Questions: 2
# WAP that takes a 2 digit number as input and print thr number which added to input number will give number in reverse digits. eg i/p: 35; o/p: 18// because 35 +18 =53

var1=int(input("Enter the number: "))
var2=var1%10
var3=var1//10
var4=var2*10+var3
print(var4-var1) 




