print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? "))

tip = int(input("What percent you will share 10, 12 or 15? "))

people = int(input("How many people share the bill? "))

bill_with_tip = tip/100 * bill + bill

bill_per_person = bill_with_tip / people

print(bill_per_person)




