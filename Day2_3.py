

age = input("Enter your current age: ")

age_as_int = int(age)

years_remaining = 90 - age_as_int
months_remaining = years_remaining * 12
weeks_remaining = years_remaining * 52
days_remaining = years_remaining * 365

message = print(f"years remaining = {years_remaining}, months remaining = {months_remaining}, weeks remainin = {weeks_remaining}, days remaining = {days_remaining}")

