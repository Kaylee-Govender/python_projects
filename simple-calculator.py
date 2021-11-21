first_number = float(input("Enter a number: "))
operation = input("Enter an operation: ")
second_number = float(input("Enter a another number: "))

if operation == "+":
    print(first_number + second_number)
elif operation == "-":
    print(first_number - second_number)
elif operation == "*":
    print(first_number * second_number)
elif operation == "/":
    print(first_number / second_number)
else: print("Invalid opperation")