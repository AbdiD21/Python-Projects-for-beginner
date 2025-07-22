def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

print("📟 Welcome to the Simple Calculator!")
print("Available operations: +  -  *  /")
print("Type 'exit' anytime to quit.\n")

while True:
    try:
        first = input("Enter the first number: ")
        if first.lower() == "exit":
            print("👋 Goodbye!")
            break
        num1 = float(first)

        second = input("Enter the second number: ")
        if second.lower() == "exit":
            print("👋 Goodbye!")
            break
        num2 = float(second)

        operator = input("Enter operator (+, -, *, /): ")
        if operator.lower() == "exit":
            print("👋 Goodbye!")
            break

        if operator == "+":
            result = add(num1, num2)
        elif operator == "-":
            result = subtract(num1, num2)
        elif operator == "*":
            result = multiply(num1, num2)
        elif operator == "/":
            result = divide(num1, num2)
        else:
            result = "Invalid operator!"

        print("➡️ Result:", result, "\n")

    except ValueError:
        print("❌ Please enter valid numbers.\n")
