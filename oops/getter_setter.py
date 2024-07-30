# class person:
#     def __init__(self,name,last,add):
#         self.name=name
#         self.last=last
#         self.address=add
#         self.mail=self.name +"."+self.last+"@gmail.com"
#     def full(self):
#         return self.name+" "+self.last+" "+self.address

# ab=person("sachin","tendulkar","munbai")
# print(ab.full())
# print(ab.mail)
# ab.address="chennai"
# print(ab.full())

##################################################
class person:
    def __init__(self,name,last,add):
        self.name=name
        self.last=last
        self.address=add
        self.mail=self.name +"."+self.last+"@gmail.com"
    def full(self):
        return self.name+" "+self.last+" "+self.address

ab=person("sachin","tendulkar","munbai")
print(ab.full())
print(ab.mail)
ab.address="chennai"
ab.last="tiger"
print(ab.last)
print(ab.mail)
print(ab.full())

################################################

#########################################################

# class person:
#     def __init__(self,name,last,add):
#         self.name=name
#         self.last=last
#         self.address=add
        

#     def email(self):
#         return self.name +"."+self.last+"@gmail.com"
    
#     def full(self):
#         return self.name+" "+self.last+" "+self.address

# ab=person("sachin","tendulkar","munbai")
# print(ab.full())
# print(ab.email())
# ab.address="chennai"
# print(ab.full())

########################################################
# class person:
#     def __init__(self,name,last,add):
#         self.name=name
#         self.last=last
#         self.address=add
        
#     @property
#     def email(self):
#         return self.name +"."+self.last+"@gmail.com"
    
#     @property
#     def full(self):
#         return self.name+" "+self.last+" "+self.address
    

# ab=person("sachin","tendulkar","munbai")
# print(ab.full)
# print(ab.email)
# ab.address="chennai"
# print(ab.full())

#########################################################
# class person:
#     def __init__(self,name,last,add):
#         self.name=name
#         self.last=last
#         self.address=add
        
#     @property
#     def email(self):
#         return self.name +"."+self.last+"@gmail.com"
    
#     @property
#     def full(self):
#         return self.name+" "+self.last+" "+self.address
    
#     @full.setter
#     def full(self,name):
#         self.name,self.last=name.split()
    
#     @full.deleter
#     def full(self):
#         self.name=None
#         self.last=None
#         print("delete successfully")

# ab=person("sachin","tendulkar","munbai")
# print(ab.full)
# print(ab.email)
# ab.address="chennai"

# ab.full="ms Dhoni"
# print(ab.email)
# print(ab.full)

# # del ab.full

# print(ab.full)