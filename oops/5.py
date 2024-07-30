# from abc import ABC, abstractmethod
# class democlass(ABC):
#    @abstractmethod
#    def method1(self):
#       print ("abstract method")

#    def method2(self):
#       print ("concrete method")

# class concreteclass(democlass):
#    def method1(self):
#       print("second")
#       super().method1()
      
      
# obj = concreteclass()
# obj.method1()
# obj.method2()


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




