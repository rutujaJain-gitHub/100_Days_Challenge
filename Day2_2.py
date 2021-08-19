

weight = input("Enter your weight:  ")
height = input("Enter your height:  ")
weight_one = float(weight)
height_one = float(height)

bms = float(weight_one) / float(height_one) ** 2

print(round(bms,2))



score = 0
height = 1.57
isWinning = True
#f-String
print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")