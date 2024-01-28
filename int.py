flat_number = int(input('Введите номер квартиры: '))

entrance_number = (flat_number - 1) // 20 + 1
floor_number = (flat_number - 1) % 20 // 4 + 1

print('Подъезд номер:', entrance_number)
print('Этаж:', floor_number)