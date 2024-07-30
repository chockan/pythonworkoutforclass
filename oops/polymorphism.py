#overloading
def abc(x,y,z=0):
    print(x+y+z)

abc(3,2)
abc(3,4,5)

#####################################
#overriding
class animal():
    def sound(self):
        print("animal makes sound")
class dog(animal):
    pass
    # def sound(self):
    #     print("dogs barks")
d1=dog()
d1.sound()

###############################3

# ploymorphism
# two types
# 1.compiler time polymorphism
 # Overloading same function name , but different signatures
# 2. run time polymorphism
    #overriding same function name,name signature but different classes connected through inheritance.
#overloading
print(len("hello"))
print(len([1,2,3,4]))
print(len((1,2,3,4)))

#overloading in class

class abcd:
    def comp(self,x=0,y=0):
        if (x==100 and y==200):
            return x*y
        elif (x==100):
            return x*x
        elif(y==200):
            return y*y
        else:
            return 0
c=abcd()
print(c.comp())
print(c.comp(100))
print(c.comp(100,200))
print(c.comp(0,200))
print(c.comp(1))
