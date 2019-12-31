""" try: 
    text = input("enter something --> ")
except EOFError:
    print("You pressed ctrl + d")
except KeyboardInterrupt:
    print("You pressed ctrl + c")
else:
    print(f'You entered {text}') """


# You can create your own exception type

class ShortInputException(Exception):
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast

try: 
    text = input ("Enter something --> ")
    if len(text) < 3:
        raise ShortInputException(len(text), 3)
except EOFError:
    print("EOFError")
except ShortInputException as ex:
    print(('ShortInputException: The input was ' + '{0} long, expected at least {1}').format(ex.length, ex.atleast))
else:
    print('No exception raised')
