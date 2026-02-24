
sub1 = float(input("Enter marks for subject 1 (out of 100): "))
sub2 = float(input("Enter marks for subject 2 (out of 100): "))
sub3 = float(input("Enter marks for subject 3 (out of 100): "))
sub4 = float(input("Enter marks for subject 4 (out of 100): "))
sub5 = float(input("Enter marks for subject 5 (out of 100): "))


total_marks = sub1 + sub2 + sub3 + sub4 + sub5
percentage = (total_marks / 500) * 100

if percentage >= 90:
    grade = "A (Outstanding)"
elif percentage >= 80:
    grade = "B (Excellent)"
elif percentage >= 70:
    grade = "B+ (Good)"
elif percentage >= 60:
    grade = "C (Average)"
else:
    grade = "F (Fail)"

status = "Pass" if percentage >= 40 else "Fail"

# Display results
print(f"\nTotal marks: {total_marks}/500")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")
print(f"Result: {status}")
