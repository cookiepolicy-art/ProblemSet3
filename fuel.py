# Fuel gauges indicate, often with fractions, just how much fuel is in a tank.
#  For instance 1/4 indicates that a tank is 25% full, 1/2 indicates that a tank is 50% full,
#  and 3/4 indicates that a tank is 75% full.

# Implement a program that prompts the user for a fraction, formatted as X/Y, 
# wherein each of X and Y is an integer, and then outputs, as a percentage rounded to the nearest integer,
#  how much fuel is in the tank. If, though, 1% or less remains,
#  output E instead to indicate that the tank is essentially empty.  
# And if 99% or more remains, output F instead to indicate that the tank is essentially full. 
# If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again.
#  (It is not necessary for Y to be 4.) 
# Be sure to catch any exceptions like ValueError or ZeroDivisionError.

def main():
    #need these to avoid 'UnboundLocalError' (which is basically out of scope) on the
    # if x > y line just below.
    x = -1
    y = -1
    while True:
        gauge = input("Fraction: ")
        x_val,y_val = gauge.split("/")
        try:
            x = int(x_val)
            y = int(y_val)
            if y == 0:
                raise ZeroDivisionError

            if x > y:
                raise ValueError
        except ValueError:
            if x > y:
                print("x must be less than y")
            else:
                print("x and y must be integers")
        except ZeroDivisionError:
            print("y must not be 0")
        else:
            break

    level = x/y
    level_percent = level * 100
    #formatted_number = "Gauge reads {0}%".format(level)
    message = "{:.0f}%".format(level_percent)
    

    if  level < 0.01:
        print("E")
    elif level >0.99:
        print("F")
    else:
        print(message)
        #print(f"level is {formatted_number}")

    # while True:
    #     gauge = input("Fraction: ")
    #     x, y = gauge.split("/")
    #     # if is_integer(x) and is_integer(y):
    #     #     print(f"You entered {x}/{y}")
    #     #     if x > y:
    #     #         raise ValueError("x must be < y")
    #     #     if y == 0:
    #     #         raise ZeroDivisionError("y can not be 0")
    #     #     show_gas_level(x,y)
    #     if input_meets_criteria(x,y):
    #         show_gas_level(x,y)

# def show_gas_level(x,y):
#     '''expects x < y, y != 0, and both x and y are integers'''
#     level = x/y
#     formatted_number = "{:0.f}".format(level)
#     if level < 0.01:
#         print("E")
#     elif level > 0.99:
#         print("F")
#     else:
#         print(formatted_number)

# def input_meets_criteria(x,y):
#     if is_integer(x) and is_integer(y):
#         print("both x,y are integers")
#         if correct_magnitudes(x,y):
#             print("both have correct mags")
#             if y_not_zero(x,y):
#                 print("y not 0")
#                 return True
#             else:
#                 print("y is 0")
#                 return False

# def y_not_zero(x,y):
#     try:
#         _ = int(x)/int(y)
#     except ZeroDivisionError:
#         return False
    
# def correct_magnitudes(x,y):
#     try:
#         if x < y:
#             return True
#     except ValueError:
#         return False
    
# def is_integer(value):
#     try:
#         int(value)
#         return True
#     except ValueError:
#         return False

main()
