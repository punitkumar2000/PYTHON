#SINGLE INHERITANCE

# class Parent_class_Name:
#Parent_class code block
# class Child_class_Name(Parent_class_name):
#Child_class code block

# class Parent():
#     def first(self):
#         print('Parent function')
#
# class Child(Parent):
#     def second(self):
#         print('Child function')
#
# object1 = Child()
# object1.first()
# object1.second()


# class Employee:
#     no_of_leaves = 8
#
#     def __init__(self, aname, asalary, arole):
#         self.name = aname
#         self.salary = asalary
#         self.role = arole
#
#     def printdetails(self):
#         return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"
#
# class Programmer(Employee):
#     no_of_holiday = 56
#     def __init__(self, aname, asalary, arole, languages):
#         self.name = aname
#         self.salary = asalary
#         self.role = arole
#         self.languages = languages
#
#     def printprog(self):
#         return f"The Programmer's Name is {self.name}. Salary is {self.salary} and role is {self.role}.The languages are {self.languages}"
#
# harry = Employee("Harry", 255, "Instructor")
# rohan = Employee("Rohan", 455, "Student")
#
# shubham = Programmer("Shubham", 555, "Programmer", ["python"])
# karan = Programmer("Karan", 777, "Programmer", ["python", "Cpp"])
#
# print(shubham.printprog())




