try: 
    text = input("enter something --> ")
except EOFError:
    print("You pressed ctrl + d")
except KeyboardInterrupt:
    print("You pressed ctrl + c")
else:
    print(f'You entered {text}')