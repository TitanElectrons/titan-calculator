from math import *

print("Welcome to Titan's Calculator!")
category = str.upper((input("These are the categories of functions available:\n\nA - addition, subtraction, multiplication, division, remainders\nB - absolute values, powers, minimums, maximums\nC - rounding to the highest or lowest integer\nD - square roots\n\nWhich one would you like to pick? > ")))

if category[0] == "A":
    group_a = str.upper((input("Which function would you like to do?\n\nA - Addition\nS - Subtraction\nM - Multiplication\nD - Division\nR - Remainders\n\nWhich one would you like to pick? > ")))
    if group_a[0] == "A":
        add_num1 = float(input("You have chosen addition. Enter your first number here: "))
        add_num2 = float(input("Enter your second number here: "))
        print(add_num1 + add_num2)
    elif group_a[0] == "S":
        sub_num1 = float(input("You have chosen subtraction. Enter your first number here: "))
        sub_num2 = float(input("Enter your second number here: "))
        print(sub_num1 - sub_num2)
    elif group_a[0] == "M":
        mul_num1 = float(input("You have chosen multiplication. Enter your first number here: "))
        mul_num2 = float(input("Enter your second number here: "))
        print(mul_num1 * mul_num2)
    elif group_a[0] == "D":
        div_num1 = float(input("You have chosen division. Enter the divident here: "))
        div_num2 = float(input("Enter the divisor here: "))
        print(div_num1 / div_num2)
    elif group_a[0] == "R":
        rem_num1 = float(input("You have chosen remainders. Enter the divident here: "))
        rem_num2 = float(input("Enter the divisor here: "))
        print(rem_num1 % rem_num2)
elif category[0] == "B":
    group_b = str.upper((input("Which function would you like to do?\n\nA - Absolute Values\nP - Powers\nM - Minimums\nN - Maximums\n\nWhich one would you like to pick? > ")))
    if group_b[0] == "A":
        abs_num1 = float(input("You have chosen an absolute value. Enter your number here: "))
        print(abs(abs_num1))
    elif group_b[0] == "P":
        base = float(input("You have chosen powers. Enter your base number: "))
        power = float(input("Enter the power of the base: "))
        print(pow(base, power))
    elif group_b[0] == "M":
        min_num1 = float(input("You have chosen minimums. Enter your first number here: "))
        min_num2 = float(input("Enter your second number here: "))
        print(min(min_num1, min_num2))
    elif group_b[0] == "N":
        max_num1 = float(input("You have chosen maximums. Enter your first number here: "))
        max_num2 = float(input("Enter your second number here: "))
        print(max(max_num1, max_num2))
elif category[0] == "C":
    group_c = str.upper(input("Which function would you like to do?\n\nR - Normal rounding\nH - Rounding to the highest number\nL - Rounding to the lowest number\n\nWhich one would you like to pick? > "))
    if group_c[0] == "R":
        norm_num1 = float(input("You have chosen normal rounding. Enter your number here: "))
        print(round(norm_num1))
    elif group_c[0] == "H":
        ceil_num1 = float(input("You have chosen high rounding. Enter your number here: "))
        print(ceil(ceil_num1))
    elif group_c[0] == "L":
        floor_num1 = float(input("You have chosen low rounding. Enter your number here: "))
        print(floor(floor_num1))
elif category[0] == "D":
    sqrt_num1 = float(input("You have chosen square roots. Enter the number here: "))
    print(sqrt(sqrt_num1))
else:
    print("You have entered a wrong letter. Please restart the program to use the calculator.")
