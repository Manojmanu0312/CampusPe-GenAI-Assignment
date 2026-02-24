count = int(input("How many numbers? "))

numbers = []
total = 0

for i in range(count):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)
    total += num


average = total / count
maximum = max(numbers)
minimum = min(numbers)


print(f"\nSum: {total}")
print(f"Average: {average:.2f}")
print(f"Maximum: {maximum}")
print(f"Minimum: {minimum}")
