# -*- coding: utf-8 -*-
"""Dictionary.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1BioFuO9dEy2C-XchryprbznNr5bOCoMN
"""

# 1. Inventory Tracker
# Scenario: Build an inventory tracker for a store that can help manage stock levels. The system should be able to:

# Add new items and their quantities to the inventory.
# Update the quantity of an existing item.
# Display a list of items with their current stock levels.
# Remove an item from the inventory.

# Answer me

# What data structures (lists/dictionaries) they would use and why.
# How they would handle user input and potential errors.
# Any additional features they think would improve the application.

item=[]


while True:
  print()
  print("Inventory Management Tracker")
  print()
  print("Choose form the above listed number 1 to 5: ")
  print()
  print("1. Add new items and their quantities to the inventory.")
  print("2. Update the quantity of an existing item.")
  print("3. Display a list of items with their current stock levels.")
  print("4. Remove an item from the inventory.")
  print("5. Exit")
  print()
  print()

  choice = input("Enter your choice: ")
  print()
  if choice == "1":
    print("You want to add new item.")
    print()
    item_name=input("Enter new item name= ")
    item_quantity=int(input("Enter item quantity= "))
    a={'itemm':item_name,'quantity':item_quantity}
    item.append(a)
    print(f'{item_name} having {item_quantity} quantity added to the inventory.')
    print()
  elif choice =='2':
    print("You want to update the quantity of an existing item.")
    print()
    update=input("Enter the name of the item you want to update: ")
    print()
    found=False
    for i in item:
      if i['itemm'] == update:
        new_quantity=int(input("Enter the new quantity: "))
        i['quantity']=new_quantity
        print(f"Quantity of {update} updated to {new_quantity}.")
        found=True
        break

      if not found:
        print(f"Item {update} not found in inventory.")
        break

  elif choice =='3':
    print("You want to display a list of items with their current stock levels.")
    print()
    if not item:
      print("Inventory is empty.")
    else:
      print("List of Inventory:")
      for i in item:
        print(f"{i['itemm']}: {i['quantity']}.\n")


  elif choice =='4':
    print("You want to remove an item from the inventory.")
    print()
    remove=input("Enter the name of the item you want to remove: ")
    print()
    found=False
    for i in item:
      if i['itemm'] == remove:
        item.remove(i)
        print(f"{remove} removed from inventory.")
        found=True
        break
      if not found:
        print(f"Item {update} not found in inventory.")
        break
  elif choice =='5':
    print("Exiting the program.")
    break

  else:
    print("Invalid choice. Please try again.")
    break

# What data structures (lists/dictionaries) they would use and why.
ANS:
It basically using empty list at first where all the new data entered by the user are stored in dictionary format as item name is kept as key itemm and value is stored and item quantity is kept as key quantity and value is stored which means its dictionary inside a list and all the data are fetch according to it as required.

# How they would handle user input and potential errors.
ANS:
There are different options:
if user choose option 1 then user had to add new item with item name and quantity and it is stored in dictionary and appended in list which is made empty at the beginning.
So in this way input of the user is handed and stored in the dictionary inside list format.

Error handle:

1. Add new items and their quantities to the inventory.
the user is asked about the item name and quantity and stored in dictionary and the dictionary is stored in the empty list which is already created at the beginning.

2. Update the quantity of an existing item.

Firstly user write the name of the item they want to update
then a variable with any name(found) is made false to check whether the item is in the list or not.
then it is checked and if found then it is updated and the variable (found) is made true and the loop is broken.. it is because found is true than its signal that the item is already found and if the item is not found then the found remains same as false.and
And in another step it is checked if the found is false or true by writting if not found and not indicates opposite and the result is printed if found is False as if not found takes just opposite as not is used which mean true.


3. Display a list of items with their current stock levels.

In this all the items stored in the dictionary are printed with their quantity.
firstly it is checked if the list is empty or not using if not item..If its true it means there is no item in the list and its false then it moves to else which means the loops runs and all the item in the list are printed.

4. Remove an item from the inventory.

Firstly user write the name of the item they want to remove
then a variable with any name(found) is made false to check whether the item is in the list or not.
then it is checked and if found then it is removed and the variable (found) is made true and the loop is broken.. it is because found is true than its signal that the item is already found and if the item is not found then the found remains same as false.and
And in another step it is checked if the found is false or true by writting if not found and not indicates opposite and the result is printed if found is False as if not found takes just opposite as not is used which mean true.


5. Exit
if the user enters any number except 1 to 5 then the programs prints Invalid choice. Please try again.

# Any additional features they think would improve the application.

1. Using of breaking lines (\n) and as well as print() for proper formatting.

2. Removing all the items listed at once should be added as a option using clear function.

3. Removing old name of the key and adding new name of the key.