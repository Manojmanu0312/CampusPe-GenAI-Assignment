print("Enter first number:", end=" ")
num1 = float(input())
print("Enter second number:", end=" ")
num2 = float(input())


add = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2 if num2 != 0 else "Error (divide by zero)"
mod = num1 % num2


print(f"{num1} + {num2} = {add}")
print(f"{num1} - {num2} = {sub}")
print(f"{num1} * {num2} = {mul}")
print(f"{num1} % {num2} = {mod}")
print(f"{num1} / {num2} = {div}") 