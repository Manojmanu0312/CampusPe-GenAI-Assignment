text = input("Enter word/number: ").lower().replace(" ", "")

print(f"Original: {text}")
print(f"Reversed: {text[::-1]}")


if text == text[::-1]:
    print("Result: PALINDROME")
else:
    print("Result: NOT PALINDROME")
