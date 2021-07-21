names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
print(names[2])
print(names[-1])
print(names[2:])
print(names[2:4])

highest = max([1, 2, 3, 46666, 98624, 5347])

print(highest)

# or

numbers = [3, 6, 2, 8, 4, 10]
max = numbers[0]

for number in numbers:
    if number > max:
        max = number
print(max)