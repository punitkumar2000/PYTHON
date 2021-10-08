#METHOD OVERRIDING

class Parent():

    def display(self):
        print("Inside Parent")

class Child(Parent):

    def show(self):
        print("Inside Child")

class GrandChild(Child):

    def show(self):
        print("Inside GrandChild")

g = GrandChild()
g.show()
g.display()

"""
Calling the Parent’s method
within the overridden method
"""

#BY USING THE CLASS NAME
# class Parent():
#
#     def show(self):
#         print("Inside Parent")
#
# class Child(Parent):
#
#     def show(self):
#         # Calling the parent's class
#         # method
#         Parent.show(self)
#         print("Inside Child")

# obj = Child()
# obj.show()

#BY USING SUPER()
# class Parent():
#
#     def show(self):
#         print("Inside Parent")
#
# class Child(Parent):
#
#     def show(self):
#         # Calling the parent's class
#         # method
#         super().show()
#         print("Inside Child")
#
# obj = Child()
# obj.show()
