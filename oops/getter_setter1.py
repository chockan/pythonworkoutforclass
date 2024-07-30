# class person:
#     def __init__(self,name,last):
#         self.name=name
#         self.last=last
#         self.mail=self.name +"."+self.last+"@gmail.com"


# ab=person("sachin","tendulkar")
# print(ab.mail)
# ab.last="tiger"
# print(ab.last)
# print(ab.mail)

#########################################################
# class person:
#     def __init__(self,name,last):
#         self.name=name
#         self.last=last
#         # self.mail1=self.name +"."+self.last+"@gmail.com"

#     def mail(self):
#         return self.name +"."+self.last+"@gmail.com"

# ab=person("sachin","tendulkar")
# # print(ab.full())
# # print(ab.mail)
# ab.last="tiger"
# print(ab.last)
# #print(ab.mail)
# print(ab.mail())

#########################################################

# class person:
#     def __init__(self,name,last):
#         self.name=name
#         self.last=last

#     @property
#     def mail(self):
#         return self.name +"."+self.last+"@gmail.com"

# ab=person("sachin","tendulkar")
# print(ab.mail)
# ab.last="tiger"
# print(ab.last)
# print(ab.mail)

#########################################################

# class person:
#     def __init__(self,name,last):
#         self.name=name
#         self.last=last

#     @property
#     def fullname(self):
#         return self.name +" "+self.last 
    
#     @fullname.setter
#     def fullname(self,fullname):
#         abc=fullname.split(" ")
#         print(abc)
#         self.name=abc[0]
#         self.last=abc[-1]

# ab=person("sachin","tendulkar")
# print(ab.fullname)
# ab.last="tiger"
# print(ab.last)
# print(ab.fullname)
# ab.fullname="ms Dhoni"
# print(ab.fullname)

##########################################################
####

# class ab:
#     def __init__(self,marks):
#         self.marks=marks
#     def per(self):
#         return (self.marks/600)*100
# s=ab(400)
# s.marks=450
# print(s.per())

# ###############################

# class ab:
#     def __init__(self,marks):
#         self.__marks=marks
#     def per(self):
#         return (self.__marks/600)*100
# s=ab(450)
# # s.__marks=300
# print(s.per())

###############################

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
# s.setter(300)
# print(s.getter())
# print(s.per())

############################################

# class ab:
#     def __init__(self,marks):
#         self.__marks=marks
#     def per(self):
#         return (self.__marks/600)*100
    
#     @property
#     def marks(self):
#         return self.__marks
    
#     @marks.setter
#     def marks(self,value):
#         self.__marks=value


# s=ab(400)
# s.marks=500
# print(s.marks)
# print(s.per())

#####################################################

# class ab:
#     def __init__(self,marks):
#         self.__marks=marks
#     def per(self):
#         return (self.__marks/600)*100
    
#     @property
#     def marks(self):
#         print("get value ",end='')
#         return self.__marks
    
#     @marks.setter
#     def marks(self,value):
#         print("set value",value)
#         if value < 0 or value > 600:
#             print("cannot set")
#         else:
#             self.__marks=value


# s=ab(400)
# s.marks=300
# print(s.marks)
# print(s.per())

#######################################################
#help("property")

###################################################


# class ab:
#     def __init__(self,marks):
#         self.__marks=marks
#     def per(self):
#         return (self.__marks/600)*100
    
#     def getter(self):
#         print("get value ",end='')
#         return self.__marks
    
#     def setter(self,value):
#         print("set value",value)
#         if value < 0 or value > 600:
#             print("cannot set")
#         else:
#             self.__marks=value

#     marks=property(getter,setter)


# s=ab(400)
# s.marks=500
# print(s.marks)
# print(s.per())

####################################################




