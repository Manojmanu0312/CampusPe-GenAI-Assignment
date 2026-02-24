n = int(input("Enter number: "))

if n < 0:
    print("Factorial is not defined for negative numbers")
elif n == 0:
    print("0! = 1")
else:
    fact = 1
    steps = []
    
    for i in range(1, n + 1):
        fact *= i
        steps.append(f"{i}")
    
    
    print(f"{n}! = {' × '.join(steps)} = {fact}")
