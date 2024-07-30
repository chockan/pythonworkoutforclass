# class base:
#     def __init__(self):
#         self.a=20
#     def ddd(self):
#         print("from base :",self.a)
        
# class derived(base):
#     def __init__(self):
#         super().__init__()
#         print("from derived:",self.a)

# b=base()
# b.ddd()
# print(b.a)
# b2=derived()


#############################################################

# class base:
#     def __init__(self):
#         self.__a=20
#     def ddd(self):
#         print("from base :",self.__a)
# class derived(base):
#     def __init__(self):
#         super().__init__()
#         print("from derived:",self.__a)

# b=base()
# b.ddd()
#print(b.__a)
# b2=derived()

######################################################################
# class Employee:
#     # constructor
#     def __init__(self, name, salary):
#         # public data member
#         self.name = name
#         # private member
#         self.__salary = salary

# # creating object of a class
# emp = Employee('Jessa', 10000)

# print('Name:', emp.name)
# # direct access to private member using name mangling
# print('Salary:', emp._Employee__salary)

##################################################################

# class Parrot:
#     def fly(self):
#         print("Parrot can fly")
    
#     def swim(self):
#         print("Parrot can't swim")

# class Penguin:
#     def fly(self):
#         print("Penguin can't fly")
    
#     def swim(self):
#         print("Penguin can swim")

# # common interface
# def flying_test(bird):
#     bird.fly()

# #instantiate objects
# blu = Parrot()
# peggy = Penguin()

# # passing the object
# flying_test(blu)
# flying_test(peggy)


#############################################################################
# print(len("hello"))
# print(len([1,2,3,4]))


#####################################################
# class abcd:
#     def comp(self,x=0,y=0):
#         if (x==100 and y==200):
#             return x*y
#         elif (x==100):
#             return x*x
#         elif(y==200):
#             return y*y
#         else:
#             return 0
# c=abcd()
# print(c.comp())
# print(c.comp(100))
# print(c.comp(100,200))
# print(c.comp(0,200))
# print(c.comp(1))

###########################################################

# class animal():
#     def sound(self):
#         print("animal makes sound")
# class dog(animal):
#     #pass
#     def sound(self):
#        print("dogs barks")
# d1=dog()
# d1.sound()

############################################################

# class ab:
#     def __init__(self,marks):
#         self.__marks=marks
#     def per(self):
#         return (self.__marks/600)*100
#     def setter(self,value):
#         self.__marks=value
#     def getter(self):
#         return self.__marks
    
# s=ab(400)
# print(s.per())
# s.setter(300)
# print(s.getter())
# print(s.per())

######################################################

class ab:
    def __init__(self,marks):
        self.b="hello"
        self.__marks=marks
    def per(self):
        return (self.__marks/600)*100
    
    @property
    def marks(self):
        return self.__marks
    
    @marks.setter
    def marks(self,value):
        self.__marks=value


s=ab(400)
print(s.b)
s.marks=500
print(s.marks)
print(s.per())

del s
print(s.b)

######################################################################









