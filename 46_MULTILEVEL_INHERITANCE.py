# MULTILEVEL INHERITANCE

# class Parent1:
#     pass
# class Derived1(Parent1):
#     pass
# class Derived2(Derived1):
#     pass


# class level1:
#     def first(self):
#         print('code')

# class level2(level1):  # inherit level1
#     def second(self):
#         print('with')

# class level3(level2):  # inherit level2
#     def third(self):
#         print('harry')

# obj = level3()
# obj.first()
# obj.second()
# obj.third()



class Dad:
    guitar = 22
    dance = 10
    basketball = 100

class Son(Dad):
    dance = 20
    basketball = 200

    def isdance(self):
        return f"Yes I dance {self.dance} no of times"

class Grandson(Son):
    dance = 30
    basketball = 300

    def isbasketball(self):
        return f"oh yeah!" \
            f"Yes I Play basketball very awesomely and score is {self.basketball} "

darry = Dad()
larry = Son()
harry = Grandson()

print(harry.guitar)



