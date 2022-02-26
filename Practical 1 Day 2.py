print("Welcome to tip calculator!")
bill = float(input("What was the total bil? $"))
tip = int(input("How much tip would you like to give? 10,12 or 15?"))
people = int(input("How main people to split the bill?"))
# bill_with_tip= bill * (1 + tip/100)
# print(bill_with_tip)

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_pre_preson = total_bill / people
final_amount = round(bill_pre_preson, 2)
# The round() function returns a floating point number that is a rounded version of the specified number,
# with the specified number of decimals.
print(f"Each preson should pay Doller($){final_amount}")
# Limiting floats to two decimal points(search google)
