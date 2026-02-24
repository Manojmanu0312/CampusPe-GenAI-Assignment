def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def modulus(a, b):
    if b == 0:
        return "Error: Modulus by zero"
    return a % b

def power(a, b):
    return a ** b

while True:
    print("\n=== CALCULATOR ===")
    print("1. Add(a+b)")
    print("2. Subtract(a-b)") 
    print("3. Multiply(a*b)")
    print("4. Divide(a/b)")
    print("5. Modulus(a%b)")
    print("6. Power(a^b)")
    print("7. Exit")
    
    choice = input("Enter choice (1-7): ")
    
    if choice == '7':
        print("Goodbye!")
        break
        
    if choice in ['1', '2', '3', '5', '6']:
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
    elif choice == '4':
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
    else:
        print("Invalid choice!")
        continue
    
    
    if choice == '1':
        result = add(a, b)
    elif choice == '2':
        result = subtract(a, b)
    elif choice == '3':
        result = multiply(a, b)
    elif choice == '4':
        result = divide(a, b)
    elif choice == '5':
        result = modulus(a, b)
    elif choice == '6':
        result = power(a, b)
    
    
    if isinstance(result, str):
        print(f"Result: {result}")
    else:
        print(f"Result: {result}")
