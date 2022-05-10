
age = input("What is your current age?")

max_age = 90
years_left = max_age - int(age)
months_left = years_left*12
weeks_left = years_left*52
days_left = years_left*365

print("You have " ,days_left, "days,", weeks_left, "weeks,","and", months_left, "months","left.")