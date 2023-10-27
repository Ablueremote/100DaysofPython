print("Welcome to the tip Calculator!")

# User inputs prompts
bill = float(input("What was the total bill? $"))

tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

people = int(input("How many people will split the bill? "))


# Calculations 
bill_w_tip = bill * (tip/100) + bill
split_bill = bill_w_tip / people
split_bill = round(split_bill, 2)

print(f"Each person should pay: {split_bill}")