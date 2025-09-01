num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("\nSelect an operation from the list below:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("Enter your choice (1/2/3/4): ")

if choice in ['1', '2', '3', '4']:
    if choice == '1':
        result = num1 + num2
        symbol = '+'
    elif choice == '2':
        result = num1 - num2
        symbol = '-'
    elif choice == '3':
        result = num1 * num2
        symbol = '*'
    else:  # choice == '4'
        if num2 == 0:
            print("Error! Division by zero is not allowed.")
            result = None
        else:
            result = num1 / num2
            symbol = '/'

    if result is not None:
        print(f"\nResult: {num1} {symbol} {num2} = {result}")

else:
    print("Invalid choice! Please choose a number between 1 and 4.")

print("\nThank you for using the calculator!")