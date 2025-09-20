'''

Assignment 1: Creating set from a list
    • Prompt the user to enter values separated by commas.
    • Create a list from the entered values.
    • Convert the list into a set to remove duplicate values.
    • Display both the list and the set.

'''

# list1=input("Please Enter the values: ")
# list2=list1.split(",")
# print(f'List created: {list2}')
# data= set (list2)
# print(f'Set created: {data}')


'''

Assignment 2: Create a dictionary where keys are integers from 1 to 5 and values are
their cubes

'''
# my_dict = {}
# for i in range(1,6):
#     my_dict[i] = i**3
# print("Keys  Values")
# print("---------------")

# for key, value in my_dict.items():
#     print(f'{key}  :   {value}')


'''

Assignment 3: Generate a dictionary with letters 'a' to 'e' as keys and their ASCII
values as values

'''

# lst = ['a','b','c','d','e',]
# my_dict = {}
# for ch in range(0, len(lst)):
#     my_dict[lst[ch]]=ord(lst[ch])

# print(my_dict)


'''

Assignment 4: Accept names of students from a user. Accept 1 name at a time and
ask user if new name needs to be added. If 'Yes', accept the name and add to a list. If
user says 'No', break out of the loop. (Add some duplicate names as well while
executing code)
    1. Print the list of names.
    2. Print only unique names from the list.

'''
# list1=[]
# stud=input("Please Enter Student's Name: ")
# list1.append(stud) 

# while True:
#     confirm=input("Do you want to add more student's name? (Yes/No): ").capitalize()
#     if confirm == "Yes":
#         stud=input("Please Enter Student's Name: ")
#         list1.append(stud)
#     elif confirm == "No":
#         break
#     else:
#         print("Please Enter Valid Choice")

# print(f'The list of student is: {list1}')
# print (f'The list with unique names of student is: {set(list1)}')

'''

Assignment 5: Calculator
    • Objective: Create a calculator using functions for operations addition, subtraction,
      multiplication and division. Use Functions.
    • Tasks:

    • Accept 2 values from a user to perform mathematical operation.
    • Accept operation to perform.
    • Call appropriate function based on the operation value.

'''
# num1=int(input("Please Enter Number 1: "))
# num2=int(input("Please Enter Number 2: "))
# opp=input("Please enter the operator (+,-,*,/): ")


# def add(a,b):
#     print (f'The Addition of {a}+{b}={a+b}')

# def sub(a,b):
#     print (f'The Substraction of {a}-{b}={a-b}')

# def mul(a,b):
#     print (f'The Multiplication of {a}*{b}={a*b}')

# def div(a,b):
#     print (f'The Division of {a}/{b}={a/b}')

# if opp == "+":
#     add(num1,num2)
# elif opp == "-":
#     sub(num1,num2)
# elif opp == "*":
#     mul(num1,num2)
# elif opp == "/":
#     div(num1,num2)
# else:
#     print("Please enter valid Operator ")




'''

Assignment 6: Write a program that checks whether a given string is a palindrome (a
string that reads the same backward as forward).
Input: Prompt the user to enter a string.
Logic: Remove any spaces and convert the string to lowercase. Check if the string
reads the same forward and backward.
Output:
Display whether the string is a palindrome. Use Functions

'''

# string1=input("Please Enter the string: ")
# string2 = string1.strip(" ")
# string2=string2.lower()
# if string2[::1] == string2[::-1]:
#     print(f'The word {string2} is a Palindrome')
# else: 
#     print(f'The word {string2} is NOT a Palindrome')



'''

Assignment 7: Print a Fibonacci series for numbers from 2 - 100. Use Functions

'''
# def fibo(n):
#     a,b = 0,1
#     fibo_list = []
#     while b<=n:
#         if b>=2:
#             fibo_list.append(b)
#         a, b = b, a+b
#     print (fibo_list)

# fibo(100)



'''

Assignment 8: Create Multiplication tables for 1 - 5 numbers using nested for and while loops

'''

# count=1
# while count<=10:
#     print("\n",end="")
#     for j in range(1,6):
#         print(f'{j}*{count}={count*j}\t', end="")
#     count+=1



'''

Challenge 1: Develop a program to manage an inventory system for a small
store. 
    • Input:
        o Prompt the user to enter items, their quantities, and prices.
        o Store the data in a dictionary where keys are item names, and values
          are another dictionary containing quantity and price.

    • Logic:
        o Implement functions to:

        ▪ Add new items to the inventory.
4758    ▪ Update the quantity or price of existing items.
        ▪ Calculate the total value of the inventory (sum of all items' value =
        quantity * price).

    • Output:
        o Display the current inventory.
        o Display the total value of the inventory.

'''

inventory = {
    'pen'      :{'quantity':100,'price':10},
    'pencil'   :{'quantity':90, 'price':5},
    'Books'    :{'quantity':10, 'price':250},
    'Compass'  :{'quantity':50, 'price':90},
    'Erazer'   :{'quantity':300, 'price':5},
    'Sharpner' :{'quantity':150, 'price':3},
    'Scale'    :{'quantity':100, 'price':10},

}

# item = input("Enter a Item: ")
# quant = int(input(f"Enter the quantity of {item}: "))
# price = int(input(f"Enter the price of {item}: "))


# inventory[item] = 'quantity': quant, price
# print(inventory)