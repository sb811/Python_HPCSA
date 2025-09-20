import re

'''
Assignment 1: Use re.search() and re.match().
    1. Pattern: banana
    Text: banana is my favorite fruit.
    2. Pattern: orange
    Text : I have an apple, but I want an orange.
    3. Pattern: Check if sentence starts with string ‘The’
    Text : The quick brown fox jumped over lazy dog.
    4. Pattern: quick
    Text : The quick brown fox jumped over lazy dog.
'''


# text ="banana is my favourite fruit"
# pattern= r"banana"
# obj1_get=re.search(pattern,text)
# print(f'The object searched is: {obj1_get.group()}')
# obj2_get=re.match(pattern,text)
# print(f'The object matched is: {obj2_get.group()}')



# text = "I have an apple, but I want an orange."
# pattern= r"orange"
# obj1_get=re.search(pattern,text)
# print(f'The object searched is: {obj1_get.group()}')
# obj2_get=re.match(pattern,text)
# print(f'The object matched is: {obj2_get}')



# text = "The quick brown fox jumped over lazy dog."
# pattern= r"^The"
# obj1_get=re.search(pattern,text)
# obj2_get=re.match(pattern,text)
# if obj1_get:
#     print(f'The object searched at begining is: {obj1_get.group()}')
# if obj2_get:
#      print(f'The object matched at begining is: {obj2_get.group()}')




# text = "The quick brown fox jumped over lazy dog."
# pattern= r"quick"
# obj1_get=re.search(pattern,text)
# print(f'The object searched is: {obj1_get.group()}')
# obj2_get=re.match(pattern,text)
# print(f'The object matched is: {obj2_get}')


'''

Assignment 2: To replace occurrences of a literal string with another string using re.sub().
1. Text: “Remove the word the from the sentence.”
Pattern: the
Replacement: ‘ ’
2. Text: “The quick brown fox jumps over the lazy dog.”
Pattern: lazy
Replacement: energetic
3. Text: “Change all instances of cat to dog.”
Pattern: cat
Replacement: dog

'''

# text = "Remove the word the from the sentence."
# print(f'Sentence before replacement: {text}')
# pattern = "the"
# replacement=' '
# sub_replace= re.sub(pattern,replacement,text)
# print(f'New Sentence is: {sub_replace}')

# text = "The quick brown fox jumps over the lazy dog."
# print(f'Sentence before replacement: {text}')
# pattern = "lazy"
# replacement='energetic'
# sub_replace= re.sub(pattern,replacement,text)
# print(f'New Sentence is: {sub_replace}')

# text = "Change all instances of cat to dog."
# print(f'Sentence before replacement: {text}')
# pattern = "cat"
# replacement='dog'
# sub_replace= re.sub(pattern,replacement,text)
# print(f'New Sentence is: {sub_replace}')


'''

Assignment 3: Basic String Extraction with re.findall()
1. Text: apple banana apple banana
Pattern: banana
2. Text: The dog says woof. The cat says meow. The bird says tweet.
Pattern: The
3. Text: 123 abc 123 def 123
Pattern: 123
4. Text: Hello hello helo hello
Pattern: hello

'''
# text = "apple banana apple banana"
# pattern = "banana"
# result= re.findall(pattern,text)
# print(result)

# text = "The dog says woof. The cat says meow. The bird says tweet."
# pattern = "The"
# result= re.findall(pattern,text)
# print(result)

# text = "123 abc 123 def 123"
# pattern = "123"
# result= re.findall(pattern,text)
# print(result)

# text = "Hello hello helo hello"
# pattern = "hello"
# result= re.findall(pattern,text)
# print(result)

'''
Assignment 4: Read a txt file and store your name and birthdate in the file.
'''
filename="/home/acts/Desktop/simple.txt"
with open(filename,"a")as filetext:
    filetext.write ("Name: HPCSA\n")
    filetext.write("Birthdate: 17/09/2025")
with open(filename,"r")as filetext:
    contents = filetext.read()
    print(f'Content of the file is: {contents}')


    