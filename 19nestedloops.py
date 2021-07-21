for x in range(4):
    for y in range(3):
        print(f"({x}, {y})")


numbers = [2, 2, 2, 2, 10]

for number in numbers:
    print('x' * number)

# or

for number in numbers:
    for x in numbers:
        print("x" * number)
        break

# or

for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)
