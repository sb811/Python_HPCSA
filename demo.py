# Count Occurences
# num = [12,34,54,54,67,11,12,35]
# set=list(set(num))
# dict={}
# for i in range(0,len(set)):
#     dict[set[i]] = num.count(num[i])

# print(dict)

#fibonacci
# a,b=0,1
# n = int(input("Please Enter the number you want to check: "))
# while n>b:
#     a,b=b,a+b
# if b==n or n==0:
#     print("number is a fibonacci number")
# else:
#     print("number is not a fibonacci number")


# Prime Number
# n = int(input("Enter the number you want to check"))
# if n <=1:
#     print("Number is not prime number")
# count=0
# for i in range(1,n+1):
#     if n%i==0:
#         count+=1
# if count == 2:
#     print("The Number is Prime")
# else:
#     print("The number is not prime number")


# # Palindrome
word = input("Enter a word: ")
word = word.lower()
reversed_word = word[::-1]
if word == reversed_word:
    print("Yes, it's a palindrome!")
else:
    print("No, it's not a palindrome.")













# num = [12,34,54,54,67,11,12,35]
# for i in range (0,len(num)):
#     a=num.count(num[i])
#     print(a)