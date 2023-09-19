ask = input("\nSimple calculator…\n\nChoose the action (1-4): \n 1. +\n 2. -\n 3. *\n 4. /\nYour choise: ")
if ask == "1":
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print("Result:", num1 + num2)
elif ask == "2":
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print("Result:", num1 - num2)
elif ask == "3":
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print("Result:", num1 * num2)
elif ask == "4":
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print("Result:", num1 / num2)
else:
    print("You entered the wrong action! Restart the program and try again...")
