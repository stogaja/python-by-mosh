temperature = 20

if temperature > 30:
    print('Its a hot day')
elif temperature < 10:
    print('Its a cold day')
else:
    print('Its neither hot nor cold')

# exercise

name = 200

if name < 3:
    print('Name must be at least three characters long.')

elif name > 50:
    print('Name can be a maximum of 50 characters.')

else:
    print('Name looks good.')

# or

name = input('Enter your name: ')

if len(name) > 50:
    print('Name can be a maximum of 50 characters.')
elif len(name) < 3:
    print('Name must be at least three characters long.')
else:
    print('Name looks good')