'''

Assignment 1: Accept 2 strings from a user as input. Concatenate these strings. Print
length of the resulting string.

'''

# str1= str(input("Please Enter a String: "))
# str2= str(input("Please Enter a String: "))
# print("The Concatenated string is: ", str1+str2)


'''

Assignment 2: Extract words from a sentence. Calculate length of each word. If length is
more than 5 print the word. Else print “Word is too short”.

'''

# sent = input("Enter a Sentence : ")
# list = list(sent.split(" "))

# for i in range (0, len(list)):
#     if len(list[i]) > 5:
#         print(list[i])
#     else:
#         print("Word is too Short")


'''

Assignment 3: Write a program that implements a basic to-do list where users can add,
remove, and view tasks.
Input:
    • Allow the user to add tasks to the to-do list.
    • Allow the user to remove tasks by specifying the task name.
    • Allow the user to view the current list of tasks.
Logic:
    • Use a list to store the tasks.
    • Implement a loop that continuously prompts the user to choose an action (add,
    remove, view, or exit).
Output:
    • Display the updated to-do list after each operation.

'''

# to_do_list = []

# def show(var):
#     print("\nTO-DO LIST")
#     print("-------------")
#     for view_list in to_do_list:
#         print(view_list)
#     print()
#     print()


# while True:
    
#     print (''' 
#     TO-DO LIST
#     1) Press "1" to add the Task       
#     2) Press "2" to remove the Task
#     3) Press "3" to View the TO-DO List
#     4) Press "Exit" to exit the program
#     ''')

#     num = input("Please Enter Your Choice: ")
#     num = num.lower()

#     if num=='1':
#         add_task1 = input("Enter a task to add: ").lower()
#         to_do_list.append(add_task1)
#     elif num=='2':
#         remove_task = input("Enter a task to remove it: ").lower()
#         to_do_list.remove(remove_task)
#     elif num=='3':
#         show(to_do_list)
#     elif num=='exit':
#         exit()
#     else:
#         print ("Invalid Response")    

#     print(to_do_list)    



'''

Assignment 4: Accept input from user, comma separated values. Create a tuple using
these input values (Split(), based on comma). Accept a threshold index from user, extract
values from tuple after the threshold index. Store these values in a new tuple. Print it.

'''

# sent = input("Enter a Sentence seperated with comma: ")

# sent_tuple = tuple(sent.split(","))

# threshold = int(input("Enter a Threshold Value: "))

# threshold_tuple = sent_tuple[threshold+1:]
# print(threshold_tuple)



'''

Assignment 5: Try out all String, List, Tuple, Set and Dictionary operations.

# '''
# # Strings
# string = "CDAC"
# print(string.capitalize())
# print(string.lower())
# print(string.upper())
# print(string.capitalize())
# print(string.format())

# # Lists
# list1 = [1,2,3,4,5]
# print(list1.append(6))
# print(list1.count(3))
# print(list1.insert(6,88))
# print(list1.remove(5))
# print(list1.index(3))

# # Tuples
# tup = (1,2,3,4,5,6)
# print(tup.count(1))
# print(tup.index(3))
# print(len(tup))

# # Sets
# set1 = {1,2,3,4,5,6,7,8,9,0}
# set2 = {2,4,6,8,0}
# print(set1.add(10))
# print(set1.remove(0))
# print(set1.union(set2))
# print(set1.difference(set2))
# print(set1.intersection(set2))

# # Dictionaries
# my_dict = {
#     'Brand':'BMW',
#     'Model':'M5 CS',
#     'Color':'Goblin Green',
#     'Fuel' :'Petrol'
# }
# for key in my_dict:
#     print(key)

# for val in my_dict.values():
#     print(val)

# for key, val in my_dict.items():
#     print(f'{key}:{val}')



'''

Challenge 1: Develop a program that simulates an ATM withdrawal process.
Input: Prompt the user to enter their account balance and the amount they wish to
withdraw.
Logic:

    • Check if the withdrawal amount is greater than the account balance. If so,
      display an error message.
    • If the withdrawal amount is valid, subtract it from the balance.
    • Ensure the withdrawal amount is a multiple of 10 (as ATMs typically dispense
      money in multiples of 10).

Output:

    • Display the remaining balance if the withdrawal is successful.
    • If not, display an appropriate error message (e.g., "Insufficient balance" or
    "Amount must be a multiple of 10").
    • Check if user wishes to withdraw more money, else exit

'''
# acc_bal = int(input("Enter the Account Balance: "))

# while True:
#     print('''
#     WELCOME TO THE JAGGA DAKU NATIONAL BANK

#     1) Press "1" for withdraw Money
#     2) Press "2" for Checking Balance
#     3) Press "3" for Exit
#     ''')
#     num = input("Enter the Number: ")

#     if num=="1":  
#         widraw_amount = int(input("Enter the Amount you want to Withdraw: "))
#         if widraw_amount > acc_bal:
#             print ("Insufficient balance")
#         elif widraw_amount < acc_bal and widraw_amount % 10 == 0:
#             acc_bal = acc_bal - widraw_amount
#             print(f'You have Withdrawed Rs.{widraw_amount} and the Remaining Balance is Rs.{acc_bal}')
#         elif widraw_amount % 10 != 0:
#             print("Amount must be a multiple of 10")
#     elif num=="2":
#         print(f"The Current Account Balance is Rs.{acc_bal}")
#     elif num=="3":
#         exit()
#     else:
#         print("Invalid Input Please Try Again....")



'''

Challenge 2: Write a program to generate and display the multiplication table up to 10 for
numbers 1- 10.
• Logic: Use nested for loops to calculate and display the multiplication table for the
number upto 10.
• Output: Display the multiplication table for numbers from 1 - 10 .

'''

for i in range(1,11):
    print("\n",end="")
    for j in range(1,11):
        print(f'{j}*{i}={i*j}\t', end="")




'''

'''

