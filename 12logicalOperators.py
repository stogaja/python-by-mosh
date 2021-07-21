# logical and operator

has_high_income = True
has_good_credit = True

if has_high_income and has_good_credit:
    print('Eligible for loan.')

# logical or operator

high_income = False
good_credit = True

if high_income or good_credit:
    print('Eligible for a loan.')

# logical NOT operator

is_good_credit = True
criminal_record = False

if is_good_credit and not criminal_record:
    print('Eligible for a loan.')


# AND both conditions must be true
# OR at least one condition is true
# NOT reverses any boolean value given

