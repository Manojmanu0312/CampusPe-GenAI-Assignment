
current_age_years = int(input("Enter your current age in years: "))


age_months = current_age_years * 12
age_days = current_age_years * 365
age_hours = age_days * 24
age_minutes = age_hours * 60
age_seconds = age_minutes * 60


print("Age in months:", age_months)
print("Age in days (approx):", age_days)
print("Age in hours:", age_hours)
print("Age in minutes:", age_minutes)
print("Age in seconds:", age_seconds)
