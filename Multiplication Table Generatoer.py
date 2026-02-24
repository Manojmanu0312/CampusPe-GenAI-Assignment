num = int(input("Enter number: "))
start = int(input("Enter range start: "))
end = int(input("Enter range end: "))

print(f"\n{num}x table from {start} to {end}")

for i in range(start, end + 1):
    result = num * i
    print(f"{num} x {i} = {result}")
