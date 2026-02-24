age = int(input("Enter customer age: "))
day = input("Enter day (Monday/Tuesday/...): ").lower()
num_tickets = int(input("Number of tickets: "))

if age < 12:
    base_price = 150
    category = "Child"
elif 12 <= age < 60:
    base_price = 250
    category = "Adult" 
else:
    base_price = 200
    category = "Senior"

discount = 0
if day in ["monday", "tuesday"]:
    discount = 20  # 20% discount
    discount_amount = base_price * 0.20
else:
    discount_amount = 0

price_after_discount = base_price - discount_amount

total_amount = price_after_discount * num_tickets

print(f"\n*** TICKET BREAKDOWN ***")
print(f"Category: {category}")
print(f"Base price: ₹{base_price}")
if discount > 0:
    print(f"Discount ({discount}%): ₹{discount_amount:.2f}")
print(f"Price after discount: ₹{price_after_discount}")
print(f"Total amount: ₹{total_amount}")
