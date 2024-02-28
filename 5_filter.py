# Data Filter: Write a function that takes a list of dictionaries 
# (representing people, with keys for name, age, and profession) 
# and a profession string, and returns a new list with dictionaries 
# where the profession matches the given string.

def filter_by_profession(people: list, profession: str) -> list:
    return [person for person in people if person['profession'] == profession];

'''
a = [
    {
        'name' : 'Joska',
        'age' : 27,
        'profession' : 'builder'
    },
    {
        'name' : 'Pista',
        'age' : 28,
        'profession' : 'driver'
    },
    {
        'name' : 'Geza',
        'age' : 29,
        'profession' : 'manager'
    },
        {
        'name' : 'Toni',
        'age' : 32,
        'profession' : 'driver'
    },
        {
        'name' : 'Lajos',
        'age' : 33,
        'profession' : 'driver'
    }
]
print(filter_by_profession(a, 'driver'))
'''