"""Datatypes"""

""" shoppingList = ['apple','banana','orange','milk','eggs']
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

 """

zoo = ('python', 'elephant', 'penguin')
print('Number of animals in the zoo is', len(zoo))

new_zoo = ('monkey', 'camel', zoo)
print('Number of cages in the new zoo is', len(new_zoo))
print('All animals in new zoo are', new_zoo)
print('Animals brought from old zoo are', new_zoo[2])
print('first animal brought from old zoo is', new_zoo[2][0]) #[2][0] means: third item of new_zoo, first item of that item
print('Number of animals in the new zoo is',
      len(new_zoo)-1+len(new_zoo[2]))



