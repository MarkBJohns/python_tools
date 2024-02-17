print('==============================================================')

print('INSTALLING 3RD PARTY LIBRARIES')

print('==============================================================')

#   While python has a large collection of standard libraries, there are even more third
#       party libraries that independent programmers have created and shared on their own.
#       Often these programs are useful for specific projects or even unique to a company,
#       and since they aren't standard, there's a more complex means of accessing them. The
#       way we can access these 3rd party libraries is by using the terminal command "pip3".

#   For instance, say you're working on a project that needs a simple Pokedex. There's a 3rd
#       party library called pypokedex that gives basic data on each of the Pokemon species. To
#       access this library, you can go to the terminal:

print("pip3 install pypokedex\n")

#       Depending on the security settings, you may need to enter a password, but otherwise a
#       library will be downloaded. In order to access it, like you would any other library, you can
#       use the 'import' keyword:

import pypokedex

#   Now we have a means to access a Pokemon species, and methods to get data from said Pokemon. If
#       we use a totally random number that I didn't look up prior to this to get a result I wanted:

p = pypokedex.get(dex=359)

print("p = pypokedex.get(dex=359)")
print(p)

#       And now that we were lucky enough to get the best, coolest pokemon, we can use the methods built
#       in to create a dictionary for it.

absol = {
    'name': p.name,
    'dex_no': p.dex,
    'height': p.height,
    'weight': p.weight,
    'types': p.types,
    'abilities': p.abilities,
    'base_stats': [
        {'hp': p.base_stats.hp},
        {'attack': p.base_stats.attack},
        {'defense': p.base_stats.defense},
        {'sp_atk': p.base_stats.sp_atk},
        {'sp_def': p.base_stats.sp_def},
        {'speed': p.base_stats.speed}
    ],
    'moves': [move.name for move in p.moves['sun-moon']]
}

print('\nabsol =')
print(f'{absol}')

print('====================================== \n')

#   The pip3 command is for python3, older versions of python may require you to use just "pip".

#   Another useful aspect of python packages is that it isn't localized depending on which directory
#       you downloaded it it, as once a python package is on your computer, you can use it no matter
#       where in your directory you're using python.