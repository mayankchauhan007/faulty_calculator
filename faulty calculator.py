#- Faulty Calculator
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Design a calculator which will correctly solve all the problems except
# the following ones:
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Your program should take operator  and the two numbers as input from the user
# and then return the result

no1 = int(input("Enter first number: "))
op = input("Enter operator(+,-,*,/): ")
no2 = int(input("Enter second number: "))

# Addition
if op == "+":
    if no1 == 56 and no2 == 9 or no1 == 9 and no2 == 56:
        print(no1, "+", no2, "= 77")
    else:
        result = no1 + no2
        print(no1, "+", no2, "=", result)

# Subtraction
if op == "-":
    result = no1 - no2
    print(no1, "-", no2, "=", result)

# Multiply
if op == "*":
    if no1 == 45 and no2 == 3 or no1 == 3 and no2 == 45:
        print(no1, "*", no2, "= 555")
    else:
        result = no1 * no2
        print(no1, "*", no2, "=", result)

# Division
if op == "/":
    if no1 == 56 and no2 == 6 or no1 == 6 and no2 == 56:
        print(no1, "/", no2, "= 4")
    else:
        result = no1 / no2
        print(no1, "/", no2, "=", result)
