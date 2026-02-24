year = int(input("Enter a year: "))

if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
    print(f"{year}: Leap year")
    if year % 100 == 0:
        print("Reason: Divisible by 400")
    else:
        print("Reason: Divisible by 4 and not by 100")
else:
    print(f"{year}: Not leap year")
    if year % 4 != 0:
        print("Reason: Not divisible by 4")
    elif year % 100 == 0 and year % 400 != 0:
        print("Reason: Divisible by 100 but not by 400")
