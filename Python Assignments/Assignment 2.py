'''

Assignment 1: Write a program that prints all multiples of 7 between 1 and 100.
    • If a number is also a multiple of 5, skip it using continue.
    • Stop the loop when the number exceeds 80.

'''

# for i in range(1,100):
#     if i > 80:
#         break
#     if (i % 7 == 0):
#         if (i % 5 == 0):
#             continue
#         print (i)


'''

Assignment 2: Ask the user to enter 10 numbers.
    • Use a for loop to count how many are even and how many are odd.
    • If the number is negative, ignore it using continue.
    • Print the total count of evens and odds at the end.

'''
# i=1
# even=0
# odd=0
# while i<=10:
#     var=int(input(f"Enter {i} number: "))
#     if (var<=0):
#         i=i+1
#         continue
    
#     if (var%2==0):
#         even=even+1
#     else:
#         odd=odd+1
#     i=i+1

# print(f'The total count of Even numbers is {even} ')
# print(f'The total count of Odd numbers is {odd} ')


'''
Assignment 3: Keep taking numbers from the user until they enter 0.
    • Add only the positive numbers to the sum.
    • Ignore negative numbers using continue.
    • Print the final sum when the user enters 0.

'''

# sum = 0
# while True:
#     num = int(input("Enter number: "))
#     if num==0:
#         break
#     elif num<0:
#         continue
#     else:
#         sum+=num

# print(sum)



'''

Assignment 4: Write a program to find the first number between 1 and 1000 that is divisible
by both 11 and 17.
    • Use a for loop.
    • Break when you find the first such number.

'''


# for i in range(1, 1000):
#     if (i % 11 == 0 and i % 17 == 0):
#         print(f'The First number which is divisible by both 11 & 17 is {i}')
#         break



'''

Assignment 5: Take a word from the user and print each character on a new line using a for
loop.
    • Skip vowels using continue.
    • Stop printing if you encounter the letter "z" (use break).

'''

# string=input("Enter a String: ")

# for i in string:
#     if i=="z": 
#         break
#     if i in "aeiou":
#         continue

#     print(i)



'''

Assignment 6: Take 5 integers from the user, store them in a list, and create a new list
containing their squares.

'''
# list1=[]
# list2=[]
# for i in range(1,6):
#     num=int(input("Enter a Number: "))
#     list1.append(num)
#     list2.append(num**2)  

# print(f'Orignal List is: {list1}')
# print("---------------------------------------------------------")
# print(f' New List of Sqaures is: {list2}')



'''

Assignment 7: From a given list of numbers (contains positive and negative integers),
create a new list that only contains the positive numbers.

'''

# list1 = [1,2,3,4,5,6,7,8,9,-1,-2,-5,-6,-8,-9,0,15,546,11]
# list2=[]
# for i in range(1, len(list1)):
#     if (list1[i]>0):
#         list2.append(list1[i])

# print(list2)


'''

Assignment 8: Ask the user to input a list of numbers and print the list in reverse order
(without using the built-in reverse() method).

'''

# list1=[]
# num=int(input("Enter a size of list: "))

# for i in range(1,num+1):
#     num=int(input("Enter a number: "))
#     list1.append(num)

# for i in range(len(list1)-1, -1,-1):
#     print(list1[i])


'''

Assignment 9: Given a list of words, count how many times "apple" occurs in the list.

'''


# word_list = ["mango", "apple", "banana", "strawberry", "apple", "cherry"]

# print(f'The Word Apple in the Word List has occured : {word_list.count("apple")} times.')



'''

Assignment 10: Given a list of numbers, create a new list that contains only the elements
at even index positions.

'''

# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

# for i in range(1, len(list1)):
#     if i%2==0:
#         print(list1[i])


'''

Assignment 11: Write a program to find the second largest number in a list (without using
max() ).

'''

# list1 = [100, 22, 395, 42, 45, 659, 777, 832, 96, 69]

# list1.sort()

# print(list1)
# print(list1[-2])



'''

Assignment 12: From a list of numbers, calculate the sum of all even numbers and the
sum of all odd numbers separately.

'''

# list1 = [100, 22, 395, 42, 45, 659, 777, 832, 96, 69]

# even_sum=0
# odd_sum=0

# for i in list1:
#     if i%2==0:
#         even_sum=even_sum+i
#     else:
#         odd_sum=odd_sum+i

# print("Even Sum is", even_sum)
# print("Odd Sum is ", odd_sum)




'''

Assignment 13: Write code to print a pyramid of stars in ascending order. Accept number
of rows from user.

'''
# num=int(input("enter the star: "))
# for rows in range(0,num):
#     for cols in range(0,num-rows):
#         print(end=" ")
#     for j in range(2*rows+1):
#         print("*", end="")
#     print()


'''

Challenge 1: Take two lists from the user and create a third list that contains only the
common elements.

'''
# list1=[]
# list2=[]
# list3=[]

# for i in range(1,6):
#     num1=int(input("Enter a element for 1st list: "))
#     list1.append(num1) 
# # print(list1)

# for i in range(1,6):
#     num2=int(input("Enter a element for 2nd list: "))
#     list2.append(num2) 
# # print(list2)

# for i in range(0, len(list1)):
#     if list1[i] in list2:
#         list3.append(list1[i])

# print(f'1st List is :- {list1}')
# print(f'2nd List is :- {list2}')
# print("---------------------------------------------")
# print(f'3rd List with Only Common Elements is :- {list3}')


'''

Challenge 2: Take a list and a value k from the user. Rotate the list to the left by k positions
using a loop.

'''

# list1 = [1,2,3,4,5,6,7,8]
# print(list1)
# k=int(input(" Please Enter Value 'K': "))
# l1=list1[k:]
# for i in list1[0:k]:
#     l1.append(i)
# print(l1)


'''

Challenge 3: Take an integer input from the user and print a countdown using a while loop.
    • If the countdown reaches a multiple of 13, stop immediately using break.
    • Print "Take Off!" at the end if the countdown completes without breaking.


'''
import time

num1 = int(input("Enter a number: "))

count=1
while count <= num1:
    if (count%13==0):
        print ("OOPS Counter Broke😭😭😭")
        break
    else:
        print(f'Countdown {count}')
        time.sleep(1) 
    count+=1
    if count>num1:
        print("Take Off! ✈️  ✈️  ✈️  ✈️")
