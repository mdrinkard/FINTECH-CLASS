# -*- coding: utf-8 -*-
"""
Student Do: Grocery List.

This script showcases basic operations of Python Lists to help Sally
organize her grocery shopping list.
"""

# @TODO: Create a list of groceries

print("Creating a list of Groceries...")
Groceries = ["Water", "Butter", "Eggs", "Apples", "Cinnamon", "Sugar", "Milk"]
print(Groceries)



# @TODO: Find the first two items on the list

print('The first 2 items on our Grocery list are :', Groceries[0:2])


# @TODO: Find the last five items on the list

print('The last 5 items on the list are:', Groceries[2:])


# @TODO: Find every other item on the list, starting from the second item

print('Every other item on the list starting from the 2nd item are:', Groceries[1::2])


# @TODO: Add an element to the end of the list

Groceries.append('flour')
print(Groceries)



# @TODO: Changes a specified element within the list at the given index

Groceries[3] = "gala apples"
print(Groceries)



# @TODO: Calculate how many items you have in the list

print('there are', len(Groceries),'items in the list')


# ----------------------Go to the grocery store---------------------------")

# @TODO: Find the index of the particular element name





# @TODO: Remove an element from the list based on the given element name





# @TODO: Remove an element from the list based on the given index






# @TODO: Remove the last element of the list





print("You continue on your journey purchasing groceries...")
