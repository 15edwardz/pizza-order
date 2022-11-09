# Generates the receipt
def generateReceipt(pizzaOrder):

    # Declares the variables
    pricePizza = 0.00
    totalPrice = 0.00
    xTopping = 0.00
    pizza = 0

    # Check if order is empty
    if len(pizzaOrder) == 0:
        print("You did not order anything")

    # Adds prices according to size and toppings
    else:
        print("Your order: ")
        # Tuple unpacking, (x,y) and accordingly compares the data to set a price
        for x, y in pizzaOrder:
            if x == "S":
                pricePizza += 7.99
                print(("Pizza {}: {} {:15.2f}".format(pizza + 1, x, pricePizza)))
                totalPrice += pricePizza
                pricePizza = 0.00
            elif x == "M":
                pricePizza += 9.99
                print(("Pizza {}: {} {:15.2f}".format(pizza + 1, x, pricePizza)))
                totalPrice += pricePizza
                pricePizza = 0.00
            elif x == "L":
                pricePizza += 11.99
                print(("Pizza {}: {} {:15.2f}".format(pizza + 1, x, pricePizza)))
                totalPrice += pricePizza
                pricePizza = 0.00
            elif x == "XL":
                pricePizza += 13.99
                print(("Pizza {}: {} {:14.2f}".format(pizza + 1, x, pricePizza)))
                totalPrice += pricePizza
                pricePizza = 0.00

            pizza += 1
            for listItems in y:
                print(f"- {listItems}")
            xTop = len(y)
            while xTop > 3:
                if x == "S":
                    xTopping += 0.50
                    print("Extra Topping ({}) {:8.2f}".format(x, xTopping))
                    totalPrice += xTopping
                    xTopping = 0.00
                    xTop -= 1
                elif x == "M":
                    xTopping += 0.75
                    print("Extra Topping ({}) {:8.2f}".format(x, xTopping))
                    totalPrice += xTopping
                    xTopping = 0.00
                    xTop -= 1
                if x == "L":
                    xTopping += 1.00
                    print("Extra Topping ({}) {:8.2f}".format(x, xTopping))
                    totalPrice += xTopping
                    xTopping = 0.00
                    xTop -= 1
                elif x == "XL":
                    xTopping += 1.25
                    print("Extra Topping ({}) {:7.2f}".format(x, xTopping))
                    totalPrice += xTopping
                    xTopping = 0.00
                    xTop -= 1
        tax = round(totalPrice * 0.13, 2)
        totalPrice += tax
        print("Tax: {:21.2f}".format(tax))
        print("Total: {:19.2f}".format(totalPrice))
