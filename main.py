# Listing how much $ you earned
print("""Earned amount: \n
Bubblegum: $202
Toffee: $118
Ice cream: $2250
Milk chocolate: $1680
Doughnut: $1075
Pancake: $80""", end="\n\n")

# Each item converted to an integer, but separate from its original string?
bubblegum = round(202, 2)
toffee = round(118, 2)
ice_cream = round(2250, 2)
milk_chocolate = round(1680, 2)
doughnut = round(1075, 2)
pancake = round(80, 2)

# Sum of partitions
revenue = sum((bubblegum, toffee, ice_cream, milk_chocolate, doughnut, pancake))

# Print Raw Income
print("Revenue: ${:.2f}".format(revenue), end="\n\n")

# Expenses
staff_exp = input("What was the total of your staff expenses?: $")
print("$" + staff_exp)
other_exp = input("What was the total of your other expenses?: $")
print("$" + other_exp)

# Net Income
net_income = (revenue - (int(staff_exp) + int(other_exp)))
print("Net income:", net_income)
