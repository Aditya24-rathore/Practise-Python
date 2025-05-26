
class Gparent:
    x=10
    def __init__(self,name,year,color):
        self.n=name
        self.y=year
        self.c=color

    def hello(self):
        print("hello")

class Cars(Gparent):
    x=20
    def __init__(self,name,year,color):
        self.n=name
        self.y=year
        self.c=color

    def hello(self):
        print("hello")

class Car(Cars):
    x=30
    def hello(self):
        print("HELLO")
        super().hello()

obj=Car("Maruti",2024,"Black")
obj1=Gparent("Dzire",2025,"White")
print(obj.n,obj.y,obj.c)
print(obj.n,obj.y,obj.c)
print(Car.x)
print(Cars.x)
obj.hello()