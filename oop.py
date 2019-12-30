#A class creates a new type. Objects are instances of that type.
""" So a fruit class has a variable of color that can be used by all 
kinds of fruits.
    But an apple (an object of that fruit class) has the color red,
which is only readable by that apple, not by the entire fruit class
 """
""" class Person:
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
print(p2.name) """

class Robot:
    population = 0
    def __init__(self, name):
        self.name = name
        print(f"(Initializing{self.name})")
        Robot.population += 0
    
    def die(self):
        print(f"{self.name} is being destroyed")
        Robot.population -= 0
        
        if Robot.population == 0:
            print(f"{self.name} was the last Robot")
        else:
            print("There are still {:d} robots working".format(Robot.population))
    
    def sayHi(self):
        print(f"Greetings, my masters call me {self.name}")

    @classmethod
    def howMany(cls):
        print("we have {:d} robots.".format(cls.population))



































