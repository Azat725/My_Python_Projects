person = {
    "name": "Vova",
    "age": 28,
    "city": "Moscow",
    "country": "Russia"
}

other_person = {
    "name": "Bob",
    "age": 27,
    "city": "New York",
    "country": "USA"
}

additional_person_info = {
    "job": "Software Enginner",
    "country": "England",
    "city": "London",
    "married": True,
}

person.update(additional_person_info)

#person["name"] = "Vova"
#person["age"] = 28
#person["city"] = "Moscow"

print(person)
print(type(person))
print(person["name"])
print()

for item in person.items():
    print(item)
    print(type(item))
    print()


for key in person.keys():
    print(key)
    print()

for value in person.values():
    print(value)
    print()
    
print(person == other_person)
print()

print(person.update(additional_person_info))
print()