# class Parent_class_Name_1:
#Parent_class_1 code block

# class Parent_class_Name_2:
#Parent_class_2 code block

# class Child_class_Name(Parent_class_name_1, Parent_class_name_2):
#Child_class code block

# class Base1:
#     def func1(self):
#         print("This is Base1 class")
#
# class Base2:
#     def func2(self):
#         print("This is Base2 class")
#
# class Child(Base1, Base2):
#     def func3(self):
#         print("This is Child class")
#
# obj = Child()
# obj.func1()
# obj.func2()
# obj.func3()




class Employee:
    no_of_leaves = 8
    var = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

class Player:
    var = 9
    no_of_games = 4
    def __init__(self, aname, agame):
        self.name = aname
        self.game = agame

    def printdetails(self):
        return f"The Name is {self.name}. Game is {self.game}"

class CoolProgramer(Player, Employee):

    language = "C++"
    def printlanguage(self):
        print(self.language)

harry = Employee("Harry", 255, "Instructor")
rohan = Employee("Rohan", 455, "Student")

shubham = Player("Shubham", ["Cricket"])
karan = CoolProgramer("Karan",["Cricket"])

print(karan.printdetails())
karan.printlanguage()

# print(det)
print(karan.var)

