"""Datatypes"""

shoppingList = ['apple','banana','orange','milk','eggs']
print("I have ", len(shoppingList), "items to purchase")

print("These items are:", end=' ')
for item in shoppingList:
    print(item, end=' ')