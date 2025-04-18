#Price of a house is 1M, if buyer has Good Credit then they need to put down 10%, otherwise they need to put down 20%. Print the down payment when the buyer has Good credit
price = 1000000
has_good_credit = True
if has_good_credit:
    down_payment = price * 0.1
else:
    down_payment = price * 0.2
print (f'The down payment is: {down_payment}')

# if name is less than 3 characters long then the program should print- " Name must be at least 3 characters", otherwise if its more than 30 characters long than the program  should print- "Name cant be more than 50 characters long", otherwise print- " Name looks good"
name = input("Enter your name: ")
print(len(name))
if len(name) < 3:
    print("Name must be at least 3 characters")
elif len(name) > 50:
    print("Name can't be more than 50 characters long")
else:
    print("Name looks good")


# User enters weight and says if its in kilograms or pounds, if its in kilograms the program converts it to pounds or does the otherwise.
weight = float(input("Enter your weight: "))
unit = input("(l)bs or (K)kilos: ")
print(unit)
if unit.upper() == "K":
    weight_in_lbs = weight / 0.45
    print(f"weight in pounds(lbs): {weight_in_lbs}")
elif unit.upper() == "L":
    weight_in_kg = weight * 0.45
    print(f"weight in kilogram(kg): {weight_in_kg}")
else:
    print("invalid unit")


