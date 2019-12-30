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

""" class Robot:
    #populations is a class variable
    #so we're asking how many Robots exist in total when we get population variable
    population = 0
    
    #name is an object variable, so it applies to instances of Robot, but not Robot itself
    #what's the name of this specific robot
    def __init__(self, name):
        self.name = name
        print(f"(Initializing{self.name})")
        Robot.population += 1
    
    #these methods APPLY and define instances of the Robot class
    #they are referred to with self rather than robot to indicate that they apply to instances, not Robot itself
    def die(self):
        print(f"{self.name} is being destroyed")
        Robot.population -= 1
        
        if Robot.population == 0:
            print(f"{self.name} was the last Robot")
        else:
            print("There are still {:d} robots working".format(Robot.population))
    
    def sayHi(self):
        print(f"Greetings, my masters call me {self.name}")

    @classmethod
    def how_many(cls):
        print("We have {:d} robots.".format(cls.population))

droid1 = Robot("R2-D2")
droid1.sayHi()
Robot.how_many
print(Robot.population, "R2")

droid2 = Robot("C-3PO")
droid2.sayHi()
Robot.how_many
print(Robot.population, "C-3PO")

droid1.die()
print(Robot.population)
droid2.die()
print(Robot.population) """


""" class schoolMember:
    def __init__(self, name, age):
        self.name = name
        self. age = age
        print(f'Initialized School Member: {self.name}', end=" ")

    def tell(self):
        print(f'Name: "{self.name}" Age: "{self.age}"', end=" ")
    
class Teacher(schoolMember):
    def __init__(self, name, age, salary):
        schoolMember.__init__(self, name, age)
        self.salary = salary
        print(f'(Initialized Teacher: {self.name})')
    
    def tell(self):
        schoolMember.tell(self)
        print('Salary: "{:d}"'.format(self.salary))

class Student(schoolMember):
    def __init__(self, name, age, grades):
        schoolMember.__init__(self, name, age)
        self.grades = grades
        print(f'(Initialized Student: {self.name})')

    def tell(self):
        schoolMember.tell(self)
        print(f'Grades: "{self.grades}"')

T = Teacher("Connie Anderson", 52, 60_000)
S = Student("West Kraemer", 20, 3.9)

print()

members = [T, S]

for member in members:
    member.tell() """

def reverse(text):
    return text[::-1]

def isPalindrome(text):
    return text == reverse(text)

something = input("Enter text: ")
if isPalindrome(something):
    print("Yes it is a palindrome")
else:
    print("no, it's not a palindrome")






























