print('==============================================================')

print('RASING ERRORS')

print('==============================================================')

#   As you saw in the Error handling notes, there's a 'rasie' keyword you can
#       add to your functions to preempt any error responses. This allows you to 
#       quickly and directly bring up any problems with the user input to allow a
#       more efficient adaption on their end.

def starter_types(pokemon):
    if not isinstance(pokemon, str):
        raise TypeError('Input must be a string')
    
    pokemon_list = [
        {'name': 'Bulbasaur', 'type': 'Grass', 'region': 'Kanto'},
        {'name': 'Chikorita', 'type': 'Grass', 'region': 'Johto'},
        {'name': 'Treecko', 'type': 'Grass', 'region': 'Hoenn'},
        {'name': 'Charmander', 'type': 'Fire', 'region': 'Kanto'},
        {'name': 'Cyndaquil', 'type': 'Fire', 'region': 'Johto'},
        {'name': 'Torchic', 'type': 'Fire', 'region': 'Hoenn'},
        {'name': 'Squirtle', 'type': 'Water', 'region': 'Kanto'},
        {'name': 'Totodile', 'type': 'Water', 'region': 'Johto'},
        {'name': 'Mudkip', 'type': 'Water', 'region': 'Hoenn'}
    ]    

    for p in pokemon_list:
        if p['name'] == pokemon:
            return {'type': p['type'], 'region': p['region']}
    
    raise ValueError('Pokemon is not a starter Pokemon')

print(f'''
def starter_types(pokemon):
    if not isinstance(pokemon, str):
        raise TypeError('Input must be a string')
      
    pokemon_list = [
        {{'name': 'Bulbasaur', 'type': 'Grass',: 'region': 'Kanto'}},
        {{'name': 'Chikorita', 'type': 'Grass', 'region': 'Johto'}},
        {{'name': 'Treecko', 'type': 'Grass', 'region': 'Hoenn'}},
        {{'name': 'Charmander', 'type': 'Fire', 'region': 'Kanto'}},
        {{'name': 'Cyndaquil', 'type': 'Fire', 'region': 'Johto'}},
        {{'name': 'Torchic', 'type': 'Fire', 'region': 'Hoenn'}},
        {{'name': 'Squirtle', 'type': 'Water', 'region': 'Kanto'}},
        {{'name': 'Totodile', 'type': 'Water', 'region': 'Johto'}},
        {{'name': 'Mudkip', 'type': 'Water', 'region': 'Hoenn'}}
    ]
      
    for p in pokemon_list:
        if p['name'] == pokemon:
            return {{'type': p['type'], 'region': p['region']}}
      
    raise ValueError('Pokemon is not a starter Pokemon)
''')

#       This function would still "work" without the raise keywords, but it would
#       simply return None as a default if you enter something like starter_types(7)
#       or starter_types('Absol'). By adding a raise keyword, you're allowing the
#       function to give a specific response to incorrect data, telling the user
#       which data would solve the issue:

print(f'stater_types(7) = "Input must be a string"')
#       "Input must be a string"

print(f'starter_types("Absol") = "Pokemon is not a starter Pokemon"')
#       "Pokemon is not a starter Pokemon"

print('====================================== \n')

#   Take this collection of code. You have a database with several people and their
#       ages:

from_my_db = [
    {'name': 'Charlie', 'age': 83},
    {'name': 'Steven', 'age': 73},
    {'name': 'Sue', 'age': 64},
    {'name': 'Peter', 'age': 71},
    {'name': 'Donna', 'age': 62}
]

#       A function to extract just the age values from the database:

def get_ages(db):
    ages = []
    for i in db:
        ages.append(i['age'])

    return ages

#       A function to find the average of a list of numbers, which a caveat that the
#       number cannot be negative or over 100:

def bounded_avg(nums):
    '''Return average of nums input'''

    for num in nums:
        if num < 1 or num > 100:
            raise ValueError("Numbers must be between 1-100")
        
    return sum(nums) / len(nums)

#       And a function that taken in all the previous data and returns a string
#       with the average you were looking for:

def handle_data():
    "Process data from our database"

    ages = get_ages(from_my_db)

    try:
        avg = bounded_avg(ages)
        print(f'The average age is {avg}')
    
    except ValueError as exc:
        print("Invalid age in list of ages")

#   Given the specific data, running the handle_data() function will return 70.6:
        
print(f'from_my_db = {from_my_db} \n')

handle_data()

print('====================================== \n')

#   But if there was an issue with the database that would prevent the bounded_avg()
#       function from running, such as a person having an age over 100:

from_my_db = [
    {'name': 'Charlie', 'age': 83},
    {'name': 'Steven', 'age': 73},
    {'name': 'Sue', 'age': 64},
    {'name': 'Peter', 'age': 71},
    {'name': 'Donna', 'age': 62},
    {'name': 'Phillip', 'age': 101}
]

#       There's nothing intrinsic to handle_data() that will explain why the
#       function wouldn't work, it would just return the ValueError from
#       bounded_avg(). In this particular case, it's somewhat intuitive to see the
#       ages as the number in "Numbers must be between 1-100", but other cases may
#       not be so obvious and it's best practice to be as specific as possible.

#   They way we can do this is by adding an 'except' block in handle_data() that's
#       looking for a specific type of error, in this case the ValueError that
#       bounded_avg() would create. From there, we can return an error message from
#       handle_data() directly rather than secondhand from a callback function:

print(f'from_my_db = {from_my_db} \n')

handle_data()