print("Welcome to the tip calculator")
bill = int(input("What was the total bill? ₹"))
tip_percent = int(input("What percentage of tip would you like to give? "))
people = int(input("How many people to split the bill between? "))

total = (bill * (tip_percent / 100)) + bill
expense = total / people
print(f"Each person should pay ₹{round(expense)} \n")