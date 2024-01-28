leb_numbers = []
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers:
    if num % 2 == 0:
        leb_numbers.append('even')
    else:
        leb_numbers.append('not even')
        
print(leb_numbers)
print()

square_dict = {x: x ** 2 for x in range(10)}
print(square_dict)

