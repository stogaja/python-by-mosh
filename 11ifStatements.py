is_hot = False
is_cold = False
if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("Its a cold day")
    print("Wear warm clothes")
else:
    print("Its a lovely day")
print("Enjoy your day")

# exercise

good_credit = True

if good_credit:
    print("you need 10% down payment")
    print(0.1 * 1000000)
else:
    print("You need 20% down payment")
    print(0.2 * 1000000)

# or

price = 1000000
has_good_credit = True

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Your down payment is: ${down_payment}.")