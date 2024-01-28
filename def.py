numbers1 = [1, 2, 3, 4, 5]
numbers2 = [6, 7, 8, 9, 10]


def find_averenge(numbers):
    averenge = sum(numbers) // len(numbers)
    return averenge
    
averenge_1 = find_averenge(numbers1)
averenge_2 = find_averenge(numbers2)

print(averenge_1)
print(averenge_2)
print()


def count_vowels(string):
    VOWELS = "AEUIOaeuio"
    count = 0
    for char in string:
        if char in VOWELS:
            count += 1
    return count

print(count_vowels("Hello world"))
print(count_vowels("Python is a very powerful language"))
print()


def nothing(): #Функция ничего не делает
    pass #заглушка

nothing()

def format_data(*, day: int, month: str) -> str: # -> используется для указания выводимого типа данных
    return f"The day is {day} of {month}"

#day = int(input("Enter a day: "))
#month = str(input("Enter a month: "))

#print(format_data(day, month))

print(format_data(day = 23, month = "February"))
print()


def add_all(*args): 
    summary = 0
    for num in args:
        summary += num
    return summary
    
print(add_all(1, 2, 3))
print()

def introduse(**kwargs):
    for key, value in kwargs.items():
        print(key)
        print(value)
        print()
        
person = {
    "name": "Bob",
    "age": 27,
    "city": "New York",
    "country": "USA"
}
    
introduse(**person)


def func_with_all_arguments(x: int, y: int, *args, value: int = 6, **kwargs):
    print(x, y)
    print(args)
    print(value)
    print(kwargs)
    
func_with_all_arguments(x = 1, y = 3, args = 5, **person)
print()

def modify_dict(old_dict: dict,**kwargs) -> tuple[dict, bool]:
    is_modifed = False
    
    for key, value in kwargs.items():
        if old_dict.get(key) != value:
            old_dict[key] = value
            is_modifed = True
    
    return old_dict, is_modifed

product = {
    "id": 1,
    "name": "MacBook",
    "price": 999.99
}

structure = modify_dict(old_dict = product, in_stock = True)

print(structure)
print(type(structure))

