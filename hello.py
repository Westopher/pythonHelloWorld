
""" print("hello world")
print("test")
print("saving?")

age = 20
name = 'West'

print(f'{name} was {age} years old when he wrote this book')

sport = "soccer"
skill = "nutmeg"

print(f"West is so nice at {sport}, he {skill}s people all the time")
 """


""" i = 5
print(i)

i = i + 1
print(i)

multiLineString = '''This is the first line.
This is the second line'''

print(multiLineString) """

""" length = 10
width = 5

area = length * width
print('Area is', area)

perimeter = 2 * (length + width)
print("Perimeter is", perimeter) """

""" number = 23
guess = int(input('Enter an integer:'))

if guess == number:
    print("you guessed it")
    print("no prize though")
elif guess < number:
    print("Nope, your guess is a little lower than the number")
else:
    print("you guess was too high")

print("done")

num = int(input("enter number"))
if num%2 == 0:
   if num%3 == 0:
      print ("Divisible by 3 and 2") #both
   else:
      print ("divisible by 2 not divisible by 3") #just the top if
else:
   if num%3 == 0:
      print ("divisible by 3 not divisible by 2")
   else:
      print  ("not Divisible by 2 not divisible by 3") """

""" number = 23
running = True

while running:
    guess = int(input('enter integer '))

    if guess == number:
        print("you got the right number")
        running = False #while loop stops running when it gets here and goes to last else below
    elif guess < number:
        print("no, the number guessed is too low")
    else:
        print("no the number is too high")
else:
    print("the while loop is donzo") """

""" for i in range(0,50,2):
    print(i)
else:
    print("loop's done") """

"""
while True:
    s = input("Say Something : ")
    if s == "quit" or s == "Quit":
        break
    print("length of string is", len(s))
print("Done")
"""


"""
If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird
"""

"""
n = int(input().strip())
if n % 2 != 0:
    print("Weird")
elif n > 1 and n < 6:
        print("Not Weird")
elif n % 2 == 0:
    print("Not Weird")
    if n > 5 and n < 21:
        print("Weird")
elif n % 2 == 0 and n > 20:
    print("Not Weird")
"""

""" n = int(input().strip())
#if odd, print weird
if n % 2 != 0:
    print("Weird")
#if even and between 2 and 5 print not weird
if n % 2 == 0 and (n > 1 and n < 6):
    print("Not Weird")
if n % 2 == 0 and (n > 5 and n < 21):
    print("Weird")
#if n is even and larger than 20 print not weird
elif n % 2 == 0 and n > 20:
    print("Not Weird")
 """


#function
def sayHello():
    print('hello world of functions')

sayHello()

















