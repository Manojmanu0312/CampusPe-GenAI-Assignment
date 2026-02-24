
total_bill = float(input("Enter total bill: "))
tax_percent = float(input("Tax percent: "))

print("\n*** BILL BREAKDOWN ***")


tax_amount = total_bill * (tax_percent / 100)
print(f"Tax({tax_percent}%): ₹{tax_amount:.2f}")


subtotal = total_bill + tax_amount
print(f"Subtotal: ₹{subtotal:.2f}")


tip_percent = float(input("Tip percent: "))
tip_amount = subtotal * (tip_percent / 100)
print(f"Tip({tip_percent}%): ₹{tip_amount:.2f}")

grand_total = subtotal + tip_amount
print(f"Total amount: ₹{grand_total:.2f}")


people = int(input("Number of people: "))
per_person = grand_total / people
print(f"Per person: ₹{per_person:.2f}")
