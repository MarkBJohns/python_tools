print("==============================================================")

print("PACKING")

print("==============================================================")

#   In python, you can unpack iterables to be their own individual variables.

starters = ['Treecko', 'Torchic', 'Mudkip']

print(f'starters = {starters}')

#   There are already ways to extract items from a list as their own values by using brackets, but
#       unpacking allows you to separate an entire list into variables in a single line. So rather
#       than:

print(f'''
The old way:
      
    grass_starter = starters[0]
    fire_starter = starters[1]
    water_starter = starters[2],
''')

print('======================================')

#       you can instead unpacking them like:

grass_starter, fire_starter, water_starter = starters

print(f'''
By unpacking:
      
    grass_starter, fire_starter, water_starter = starters
      
and now you can get
      
    grass_starter = {grass_starter}
    fire_starter = {fire_starter}
    water_starter = {water_starter}
''')

print('======================================')

#   This is also useful for things like coordinates:

point = (15, 27)

x, y = point

#   x = 15, and y = 27

#   There's also a 'rest' keyword that lets you extract a specific value from a list as return the
#       remaining values as its own list. Say you have your standard six Pokemon team:

pokemon_team = ['Zapdos', 'Swampert', 'Metagross', 'Salamence', 'Dugtrio', 'Skarmory']

#       You can take the first value to designate it your lead pokemon and keep the remaining values
#       in their own list:

lead_pokemon, *party = pokemon_team

print(f'''
pokemon_team = {pokemon_team}

lead_pokemon, *party = pokemon_team

lead_pokemon = {lead_pokemon}

party = {party}
''')

print('======================================')

#       By using *, python knows to take in the variable name that follows and use it to store all
#       all the remaining values in that list. Note that the original list is not changed.

#   When you unpack lists in pairs, python automatically makes them tuples. For example, if you enter
#       "x, y" into your shell, it will return (15, 27), a tuple. As a better example for how it changes
#       values, look at nested lists:

color_pairs = [['red', 'green'], ['orange', 'teal']]

#       It's simple enough to get the pairs by the normal unpacking process:

pair1, pair2 = color_pairs

#       Now pair1 = ['red', 'green'] and pair2 = ['orange', 'teal'], but what if we want to get any of the
#       colors individually? We need to use tuples as we unpack:

((primary1, secondary1), (primary2, secondary2)) = color_pairs

#       This works because the unpacking process automatically generates tuples, but in nested cases, they
#       need to be explicitly coded or it won't recognize what you want, as color_pairs is technically a
#       single list with only two values, and an unpacking line with 4 variable names would be too many for
#       it.

print(f'''
color_pairs = {color_pairs}

pair1, pair2 = color_pairs

pair1 = {pair1}
pair2 = {pair2}

((primary1, secondary1), (primary2, secondary2)) = color_pairs

primary1 = {primary1}
secondary1 = {secondary1}

primary2 = {primary2}
secondary2 = {secondary2}
''')

#   One of the most common use cases is in loops, like a dictionary creating single data point for a key and
#       a value

kanto_starter = {
    'Bulbasaur': 'Grass',
    'Charmander': 'Fire',
    'Squirtle': 'Water'
}

print(f'''
Unpacking with a for loop can look something like:
      
kanto_starter = {kanto_starter}

for (pokemon, type) in kanto_starter.items():
    print(pokemon, type)
''')

for (pokemon, type) in kanto_starter.items():
    print(pokemon, type)

print('======================================')

#   Packing isn't a specific process, and in fact you've been doing it by default this entire time. If 
#       unpacking is taking a data_structure and extracting it into single values, packing is just taking
#       individual values and putting them into a data structure:

string_one = 'Hello'

string_two = 'world!'

string_list = [string_one, string_two]

#       But we also have something similar to JavaScript's 'spread' operator, in order to create newer
#       versions of existing data structures.

greeting = [*string_list, 'What a day!']

#   Now greeting will return ['Hello', 'world!', 'What a day!'], taking the value from string_list and adding
#       it to a new list. You can also add it wherever in the list you want, so the values could be added to
#       the middle or end of the list depending on which index you place it in. This works for dictionaries
#       as well, but you have to use two **, as just one will try to convert only the keys into a set.

#   For example, if we want to expand on the kanto_starter dictionary, we can create a new dictionary with
#       the additional values and the imported values from the kanto_starters:

kanto_and_johto = {
    **kanto_starter,
    'Chikorita': 'Grass',
    'Cyndaquil': 'Fire',
    'Totodile': 'Water'
}

#       This new dictionary now includes every Pokemon and type in both the Kanto and Johto regions. To see
#       how the single * works, you can see it here:

kanto_names = [*kanto_starter]

print(f'''
kanto_starter = {kanto_starter}

kanto_names = [*kanto_starter]
kanto_names = {kanto_names}

kanto_and_johto = {{
    **kanto_starter,
    'Chikorita': 'Grass',
    'Cyndaquil': 'Fire',
    'Totodile': 'Water'
}}

kanto_and_johto = {kanto_and_johto}
''')

print('======================================')

#   The star can also help you expand things like strings that can be iterated through but typically 
#       aren't:

string = "hello world"

star_string = [*string]

#       And star_string now returns ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']. This also 
#       helps to separate strings and list during printing or returning, such as a list of numbers being
#       printed individually rather than as a list:

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f'''
num_list = {num_list}

print(num_list)
{num_list}

print(*num_list)''')
print(*num_list)