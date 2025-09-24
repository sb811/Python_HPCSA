# stud_dict = {
#     'Soham' : 87,
#     'Mohit'  : 64,
#     'Yogesh' : 85
# }

# name = input("Please enter name")
# marks = float(input("Please Enter marks"))

# stud_dict[name]=marks
# print(stud_dict)

# stud_del=input("Please Enter the student you want to delete")
# del stud_dict[stud_del]
# print(stud_dict)

# sum = 0
# for value in stud_dict.values():
#     sum+=value
# print(sum)

# average = sum/len(stud_dict)
# print(f'Average Mark of Students are {average}')


# IP = "192.168.82.91"
# IP = input("Enter the IP: ")
# list = IP.split(".")
# print (list)
# n_list = []
# for i in range(0, len(list)):
#     num = list[i]
#     new_num = int(num)
#     n_list.append(new_num)

# count = 0
# for ip in range(0, len(n_list)):
#     if n_list[ip]  >= 0 and n_list[ip] <= 256:
#         count += 1
#     else:
#         print(f'The IP{IP} is not a valid ip')

# if count <= 4:
#     print(f'The IP {IP} is a Valid IP Address')
# else: 
#     print(f'The IP {IP} is a NOT a Valid IP Address')