#A class creates a new type. Objects are instances of that type.

class Person:
    def sayHi(self):
        print("hello there, world")

p = Person()
p.sayHi()

class Person2:
    def __init__(self, name, age, profession):
        self.name = 'Benedicte'
        self.age = age
        self.profession = profession
    
    def sayHello(self):
        print(f'Hey {self.name}, you are {self.age} years old, and you are a pro {self.profession}.')

p2 = Person2("West", 34, "Python dev")
print(p2.name)