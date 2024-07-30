# is used to hide the internal functionality of the function from the users.
# we need to import the abc module
#from abc import ABC ,abstractmethod


from abc import ABC, abstractmethod
class democlass(ABC):
   @abstractmethod
   def method1(self):
      print ("abstract method")
      return
   def method2(self):
      print ("concrete method")

class concreteclass(democlass):
   def method1(self):
      super().method1()
      return
      
obj = concreteclass()
obj.method1()
obj.method2()


#####################################################
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
circle = Circle(6)
rectangle = Rectangle(5,7)
print(circle.area())  # Output: 113.09724
print(rectangle.area())  # Output: 35

######################################################
from abc import ABC, abstractmethod
class Absclass(ABC):
    def print(self,x):
        print("Passed value: ", x)
    @abstractmethod
    def task(self):
        print("We are inside Absclass task")
 
class test_class(Absclass):
    def task(self):
        print("We are inside test_class task")
 
class example_class(Absclass):
    def task(self):
        print("We are inside example_class task")
 
#object of test_class created
test_obj = test_class()
test_obj.task()
test_obj.print(100)
 
#object of example_class created
example_obj = example_class()
example_obj.task()
example_obj.print(200)