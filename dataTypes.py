"""Datatypes"""

shoppingList = ['apple','banana','orange','milk','eggs']
print("I have ", len(shoppingList), "items to purchase")

print("These items are:", end=' ')
for item in shoppingList:
    print(item, end=' ')

print("\nI also have to buy rice")
shoppingList.append("rice")
print("my shopping list is now", shoppingList)

print("sort the list")
shoppingList.sort()
print("sorted list is:", shoppingList)

print("The first thing I'm gonna buy is", shoppingList[0])
oldItem = shoppingList[0]
del shoppingList[0]
print("I bought the", oldItem)
print("my list is now:", shoppingList)




