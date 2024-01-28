#цикл While может обрабатоваться бесконечное количество раз, исполняется по условию

counter = 1

while counter <= 10:
    print(f"{counter}")
    counter += 1


my_list = [0, 1, 2, 3]

while my_list:
    element = my_list.pop()
    print(element)
    
print(my_list)


#while True: бесконечный цикл
#    print("Hi")

