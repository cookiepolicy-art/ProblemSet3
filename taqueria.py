# implement a program that enables a user to place an order,
#  prompting them for items, one per line, until the user inputs control-d (control-c in windows)
# After each inputted item, display the total cost of all items inputted thus far,  
# prefixed with a dollar sign ($) and formatted to two decimal places. 
# Treat the user’s input case insensitively. Ignore any input that isn’t an item.
# Assume that every item on the menu will be titlecased.  
#   Here’s how to test your code manually: 
#    Type Taco and press Enter, then type Taco again and press Enter. 
#        Your program should output:  Total: $6.00  
#    Type Baja Taco and press Enter, then type Tortilla Salad and press enter. 
#        Your program should output: Total: $12.25 
#    Type Burger and press Enter. Your program should reprompt the user.

menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    bill = 0.0
    while True:
        try:
            #get order and check for ctrl-d (ctrl-c on Windows) to quit
            item1 = input("Item: ")
            item  = item1.rstrip().lstrip()
            order = item.title()
#            print(f"order is {order}")
            if order in menu:
#                print(f"order is in menu, it costs {menu[order]}")
                bill += menu[order]
                bill_formatted = "${:.2f}".format(bill)
                print(f"Total: {bill_formatted}")

            # else:
            #     print(f"{order} is NOT in the menu")
        except KeyboardInterrupt:  #ctrl-c caught (ctrl-d does not work in windows)
            print()  #need to move cursor down one line
            break
    bill_formatted = "${:.2f}".format(bill)
    print(f"Total: {bill_formatted}")

        



main()