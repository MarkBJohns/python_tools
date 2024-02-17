print('ERROR HANDLING')

print('==============================================================')

#   You've likely noticed by now that python is a lot quicker to give errors than JavaScript, which has its
#       own advantages. Having more errors means your code has to be stricter and more precise, which can
#       prevent you from making a complicated mess that technically does something, but that something is
#       indiscernible. One of the most common examples are for things that JavaScript would simply return
#       NaN or undefined:

#           1. Too many/few function arguments
#           2. Access an index beyond the scope of your list
#           3. Retrieve a nonexistent value from a dictionary
#           4. Use a missing attribute in an instance
#           5. Conversion failures (strings to integers, etc)
#           6. Dividing by 0

#           etc

# As a general rule, python wants you to be explicit in your code rather than implicit.

#   JavaScript has a try / catch block you can use to preempt a possible error, and python has something very
#       similar called try / except, which given python's strictness, you'll see and use a lot.

#   Say you want to see how many quarters are in a given amount of money. You want to divide it by .25, but
#       you can't divide a string, or a boolean, or a list, etc. In order to ensure this function works, or
#       barring that, moves on without crashing the whole code, you can create a 'try' for the function when
#       it runs properly, and an 'except' for what happens when the wrong value is entered:

def count_quarters(amount):
    try:
        amount = float(amount)

        quarters = int(amount // .25)
        remainder = round(amount % .25, 2)

        return f'{amount} has {quarters} quarters in it with {remainder} cents left over'
    except:
        return 'Please enter a valid dollar amount'
    
#   So if you enter count_quarters(625.13), the function will run as intended. But if you enter
#       count_quarters("hello world"), rather than an error crashing the program, you'll get a gentle 
#       reminder to try again with a number.
    
print(f'''
def count_quarters(amount):
    try:
        amount = float(amount)

        quarters = int(amount // .25)
        remainder = round(amount % .25, 2)

        return f'{{amount}} has {{quarters}} quarters in it with {{remainder}} cents left over'
    except:
        return 'Please enter a valid dollar amount'
      
count_quarters(625.13) = {count_quarters(625.13)}

count_quarters("hello world") = {count_quarters("hello world")}

count_quarters('') = {count_quarters('')}
''')

print('======================================')

#   While this is simple enough, you can run into issues where there are a million different ways to enter
#       the wrong data, and a singular error response message won't cover all the bases. Python has different
#       built in error types in order to return specific error handling messages:

#           1. AttributeError - couldn't find an attribute being searched for
#           2. KeyError - couldn't find the key being searched for
#           3. IndexError - couldn't find the index being searched for
#           4. NameError - couldn't find the variable being named for
#           5. OSError - issue with the OS, couldn't read/write the file, etc
#           6. ValueError - incorrect value (string instead of int, etc)

#   So say we have a Pokemon dictionary where we want to see if it knows an attack, and if that attack has a
#       STAB ("same type as" bonus) for that attack:

arcanine = {
    'type': 'Fire',
    'moves': [
        {'Flare Blitz': 'Fire'},
        {'Extreme Speed': 'Normal'},
        {'Close Combat': 'Fighting'},
        {'Energy Ball': 'Grass'}
    ]
}

#   This Pokemon dictionary includes a 'type' and 'moves' key, with 'moves' having a list of 
#       dictionaries. Each dictionary has the name of the move, and the type of the move. In order
#       to see if the Pokemon gets the STAB bonus for using the move, the 'type' value need to
#       match the 'moves[x].value()' value. But this function won't work unless there's a very
#       specific type of dictionary with specific data, which we have to account for in our
#       function:

def check_for_STAB(pokemon, attack):
    try:

        if pokemon['type'] is None or pokemon['moves'] is None:
            return f"{pokemon} is missing 'type' or 'moves' information."
        
        attack = attack.lower()

        for move in pokemon['moves']:
            for move_name, move_type in move.items():
                if move_name.lower() == attack:
                    if move_type.lower() == pokemon['type'].lower():
                        return True
                    else:
                        return False
                    
        raise ValueError(f'Pokemon does not learn {attack}')
    except AttributeError:
        return 'The "type" value must be a string, and "attack" must be a list of dictionaries'
    except KeyError:
        return '"Pokemon" must have a "type" and "moves" key'
    except IndexError:
        return 'Pokemon "moves" key must be a list of dictionaries'
    except NameError:
        return 'The "attack" name must be a string'
    except TypeError:
        return '"Pokemon" must be a dictionary and "attack" name must be a string'
    except ValueError as e:
        return str(e)
    
#   The function has several except conditions, to account for a variety of reasons why the 
#       Pokemon object or the move may not be valid data. It will then return True of False 
#       depending on the two type values matches. Looking at arcanine, all of his moves will
#       return False, save for Flare Blitz, the Fire type move.
    
print(f'''
def check_for_STAB(pokemon, attack):
    try:
      
        if pokemon['type'] is None or pokemon['moves'] is None:
            return f"{{pokemon}} is missing 'type' or 'moves' information."
        attack = attack.lower()

        for move in pokemon['moves']:
            for move_name, move_type in move.items():
                if move_name.lower() == attack:
                    if move_type.lower() == pokemon['type'].lower():
                        return True
                    else:
                        return False
    
        raise ValueError(f'Pokemon does not learn {{attack}}')
    except AttributeError:
        return 'The "type" value must be a string, and "attack" must be a list of dictionaries'
    except KeyError:
        return '"Pokemon" must have a "type" and "moves" key'
    except IndexError:
        return 'The Pokemon "moves" key must be a list of dictionaries'
    except NameError:
        return 'The "attack" name must be a string'
    except TypeError:
        return '"Pokemon" must be a dictionary and "attack" name must be a string'
    except ValueError as e:
        return str(e)
''')

print(f'check_for_STAB(arcanine, "Energy Ball") = {check_for_STAB(arcanine, "Energy Ball")}')

print(f'check_for_STAB(arcanine, "Close Combat") = {check_for_STAB(arcanine, "Close Combat")}')

print(f'check_for_STAB(arcanine, "Extreme Speed") = {check_for_STAB(arcanine, "Extreme Speed")}')

print(f'check_for_STAB(arcanine, "Flare Blitz") = {check_for_STAB(arcanine, "Flare Blitz")}')

print('======================================')

#   If your object doesn't have the proper data, the function now has the proper error handling to
#       tell you what data is missing:

missingNO = {
    'type': None,
    'moves': None
}

#       As MissingNo has no data to search for, it's immediately caught by the 'if' conditional
#       and a string is returned rather than an error.

print(f'missingNO = {missingNO}')
print('--------------------------------------')
print('check_for_STAB(MissingNO, "Hyper Beam") =')
print(check_for_STAB(missingNO, "Hyper Beam"))
print('======================================')

#       If a Pokemon has no 'moves' key to go through, the KeyError activates:

crobat = {
    'type': ['Poison', 'Flying'],
}

print(f'crobat = {crobat}')
print('--------------------------------------')
print('check_for_STAB(crobat, "Wing Attack") =')
print(check_for_STAB(crobat, "Wing Attack"))
print('======================================')

sceptile = {
    'type': 100,
    'moves': [
        {'Leaf Blade': 'Grass'},
        {'Thunder Punch': 'Electric'},
        {'Dragon Breath': 'Dragon'},
        {'Quick Attack': 'Normal'}
    ]
}

print(f'sceptile = {sceptile}')
print('--------------------------------------')
print('check_for_STAB(sceptile, "Leaf Blade") =')
print(check_for_STAB(sceptile, "Leaf Blade"))
print('======================================')

tauros = [{'type': 'Normal'}, {'moves': [
    {'Earthquake': 'Ground'},
    {'Body Slam': 'Normal'},
    {'Close Combat': 'Fighting'},
    {'Hyper Beam': 'Normal'}
]}]

print(f'tauros = {tauros}')
print('--------------------------------------')
print('check_for_STAB(tauros, "Body Slam") =')
print(check_for_STAB(tauros, "Body Slam"))
print('======================================')

pikachu = {
    'type': 'Electric',
    'moves': ['Volt Tackle', 'Energy Ball', 'Quick Attack', 'Surf']
}

print(f'pikachu = {pikachu}')
print('--------------------------------------')
print('check_for_STAB(pikachu, "Surf") =')
print(check_for_STAB(pikachu, "Surf"))
print('======================================')

alakazam = {
    'type': 'Psychic',
    'moves': [
        {1: 'Ice'},
        {2: 'Electric'},
        {3: 'Psychic'},
        {4: 'Fire'}
    ]
}

print(f'alakazam = {alakazam}')
print('--------------------------------------')
print('check_for_STAB(alakazam, "Fire Punch") =')
print(check_for_STAB(alakazam, "Fire Punch"))
print('======================================')

pikablu = {}

print(f'pikablu = {pikablu}')
print('--------------------------------------')
print('check_for_STAB(pikablu, "Splash") =')
print(check_for_STAB(pikablu, "Splash"))
print('======================================')


#       Now you can check to shell to see all of these Pokemon objects in practice, and rather 
#       than an error, it simply returns why the data was insufficient and the rest of the file
#       continues to run.