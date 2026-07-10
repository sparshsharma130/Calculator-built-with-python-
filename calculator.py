# your code starts here
x = int(input("enter a number: "))
operation = input("what's the operation you wanna do?")
y = int(input("enter your next one:"))
if operation == "+":
    print(x + y)
elif operation == "-":
    print(x - y)
elif operation == "*":
    print(x * y)
elif operation == "/":
    print(x / y)
elif operation == "**":
    print(x ** y)
else:
    print("invalid operation")
