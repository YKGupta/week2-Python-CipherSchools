class Person:
    def __init__(self , name):
        self.name = name

    def say_hi(self):
        print('Hemlo, my name is:' , self.name)

p = Person('Yash Kumar Gupta') 
p.say_hi()

a = 1
b = (a+1)
print(b)
del a
a = 1
type(a)
class A:
    a = 1
    b = 2
    def __add__(self, x):
        return self.a + self.b+x
a = A()
print(a.__add__(10))