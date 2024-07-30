




from abc import ABC,abstractmethod

class a(ABC):
    @abstractmethod
    def method1(self):
        print("i am from class A")
        pass
    
    def method2(self):
        print("i am from method 2")

class b(a):
    def method1(self):
        print("i am from class b")
obj=b()
obj.method1()
obj.method2()