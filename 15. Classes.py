# class Car:
#     wheels = 4
#     brand = ""
#     model = ""
#     year = ""


#     def set_info(self, brand1, model1, year1):
#         self.brand = brand1
#         self.model = model1
#         self.year = year1


#     def display_info(self):
#         print(f'Car Information:\nBrand : {self.brand}\nModel : {self.model}\nYear pf Manufacturing : {self.year}\n')


# if __name__ == '__main__':  
#     car1 = Car()
#     car1.set_info("BMW", "M5CS", "2022")

#     car2 = Car()
#     car2.set_info("Audi", "RS5", "2020")


#     car1.display_info()
#     car2.display_info()



# Class Assignment 1 : Creating a Student Class

class Students:


    def set_details(self, Rollno, Name, Marks):
        self.rollno = Rollno
        self.name = Name
        self.marks = Marks

    
    def get_details(self):
        print(f'''
Students Information
---------------------
Name  : {self.name}
Roll  : {self.rollno}
Marks : {self.marks}%\n''')
        

if __name__ == '__main__': 
    std1 = Students()
    std1.set_details(21,"Soham",69)

    std2 = Students()
    std2.set_details(12, "Mohit", 67)


    std1.get_details()
    std2.get_details()