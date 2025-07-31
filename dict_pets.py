#https://stepik.org/lesson/446696/step/14?unit=437002

pets = [('Hatiko', 'Parker', 'Wilson', 50),
        ('Rusty', 'Josh', 'King', 25),
        ('Fido', 'John', 'Smith', 28),
        ('Butch', 'Jake', 'Smirnoff', 18),
        ('Odi', 'Emma', 'Wright', 18),
        ('Balto', 'Josh', 'King', 25),
        ('Barry', 'Josh', 'King', 25),
        ('Snape', 'Hannah', 'Taylor', 40),
        ('Horry', 'Martha', 'Robinson', 73),
        ('Giro', 'Alex', 'Martinez', 65),
        ('Zooma', 'Simon', 'Nevel', 32),
        ('Lassie', 'Josh', 'King', 25),
        ('Chase', 'Martha', 'Robinson', 73),
        ('Ace', 'Martha', 'Williams', 38),
        ('Rocky', 'Simon', 'Nevel', 32)]

result = {}

for pet, firstname, secondname, age in pets:
    owner = (firstname, secondname, age)
    result.setdefault(owner, []).append(pet)
print(result)
print()
###

result_2 = {}
for pet, firstname, secondname, age in pets:
    owner = (firstname, secondname, age)
    result_2[owner] = result_2.get(owner, []) + [pet]
print(result_2)