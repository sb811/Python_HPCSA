import re

'''

Assignment 1: To split a string into a list of substrings based on a literal delimiter using
re.split().
1. String: one two three
Pattern: (single space)
2. String: a.b.c.d
Pattern: .
3. String: x-y-z
Pattern: -

'''

# string = "one two three"
# pattern=" "
# split_str= re.split(pattern,string)
# print(f'String splitted from pattern "{pattern}"  : {split_str}')


# string = 'a.b.c.d'
# pattern = '\.'
# split_str=re.split(pattern,string)
# print(f'String splitted from pattern "{pattern}" : {split_str}')


# string = 'x-y-z'
# pattern = '-'
# split_str=re.split(pattern,string)
# print(f'String splitted from pattern "{pattern}"  : {split_str}')



'''

Assignment 2: Use re.search() and re.match().
1. Pattern: banana
Text: banana is my favorite fruit.
2. Pattern: orange
Text : I have an apple, but I want an orange.
3. Pattern: The
Text : The quick brown fox.
4. Pattern: quick
Text : The quick brown fox.

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

Assignment 3: To replace occurrences of a literal string with another string using re.sub().
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

Assignment 4: Basic String Extraction with re.findall()
1. Text: apple banana apple banana
Pattern: banana
2. Text: The dog says woof. The cat says meow. The bird says tweet.
Pattern: The
3. Text: 123 abc 123 def 123
Pattern: 123
4. Text: hello hello hello hello
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

Assignment 5: From given text extract product codes.
Product codes begin with a capital letter and end with 3 digits
e.g. : PQ123, AB567
Text: “Here is a list of product codes: PQ123, AN-RFT,AB567,CP-876,AK-57”

'''

# Text = "Here is a list of product codes: PQ123, AN-RFT,AB567,CP-876,AK-57"
# pattern = r"[A-Z]+\d{3}"

# matches= re.findall(pattern,Text)
# print(f'The Product Codes are : {matches}')



'''

Challenge 1: Find vowels in the string.
Text : “This string contaIns vowels”
Output : Print no of vowels in the above string.

'''

Text = "This string contaIns vowels"
pattern  = r"[aeiouAEIOU]"
vowel_list = re.findall(pattern,Text)
print(Text)
print(vowel_list)
print(f"\nNumber of vowels in the above string: {len(vowel_list)}")
print('---------------------------------------------------------------------')

'''

Challenge 2: Print no of times each vowel occurs, in the form of a dictionary

'''

vowel_count = {}

for vowel in list(set(vowel_list)):
    vowel_count[vowel] = vowel_list.count(vowel)

print("Number of times each vowel occurs is: ")
for key, value in vowel_count.items():
    print(f'{key}:{value}')

