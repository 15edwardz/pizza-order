# Imports all functions from pizzaReceipt
from pizzaReceipt import *

# Initiates lists that will be used throughout the program
TOPPINGS = ("ONION", "TOMATO", "GREEN PEPPER", "MUSHROOM", "OLIVE", "SPINACH", "BROCCOLI", "PINEAPPLE", "HOT PEPPER",
            "PEPPERONI", "HAM", "BACON", "GROUND BEEF", "CHICKEN", "SAUSAGE")
pizzaOrder = []
toppingList = []


# Starts the program and decides if user wants to continue
def startOrder():
    beginOrder = input("Do you want to order a pizza? ")
    if beginOrder.lower() == "no" or beginOrder.lower() == "q":
        return False

# Lets user choose size of their pizzas
def chooseSize():
    currentOrder = ()
    global pizzaSize
    pizzaSize = str(input("Choose a size: S, M, L or XL: ").upper())

    if pizzaSize == "S" or pizzaSize == "M" or pizzaSize == "L" or pizzaSize == "XL":
        currentOrder = (pizzaSize)
        print(currentOrder)
    else:
        print("Please enter a valid size")
        chooseSize()

# Lets user choose the toppings on the pizza
def chooseToppings():
    global toppingSelect
    toppingSelect = str(input("Type in one of our toppings to add it to the pizza. To see the list of toppings, enter"
                              " \"LIST\". When you are done adding topping, enter \"X\"\n").upper())
    if toppingSelect == "X":
        return False

# Adds toppings the toppings to a list and/or lists all the toppings for user to see
def addToOrder():
    if toppingSelect == "LIST":
        print(TOPPINGS)
    else:
        for x in TOPPINGS:
            if x in toppingSelect:
                toppingList.append(x)
                print(f"Added {x} to your pizza")
        if toppingSelect not in TOPPINGS:
            print("Invalid Topping")

# Adds the size and all the toppings to a tuple and adds the tuple to a list of all the pizzas
def addPizza():
    currentPizza = (pizzaSize, toppingList)
    pizzaOrder.append(currentPizza)

# Asks if user would like to continue ordering
def nextPizza():
    continueOrder = str(input("Do you want to continue ordering? ").upper())
    if continueOrder == "NO" or continueOrder == "Q":
        return False

# Takes the order
if startOrder() != False:
    chooseSize()
    while chooseToppings() != False:
        addToOrder()

    else:
        addPizza()

    while nextPizza() != False:
        chooseSize()
        toppingList = []
        while chooseToppings() != False:
            addToOrder()
        else:
            addPizza()
    generateReceipt(pizzaOrder)
else:
    generateReceipt(pizzaOrder)


