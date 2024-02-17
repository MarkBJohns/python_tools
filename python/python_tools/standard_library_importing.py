print('==============================================================')

print('STANDARD LIBRARY AND IMPORTING')

print('==============================================================')

#   Like JavaScript has jQuery, python has several libraries that import new
#       code and methods that aren't in base python. As python is generally a
#       slower language and works in several environments other than web browsers,
#       it's useful to keep code segregated into different libraries. One common
#       example would be code you want to run on a Windows OS rather than a Mac OS.

#   Unlike JavaScript, there's no source link you have to use to access a python
#       library. As python is a program you have to download, all of these libraries
#       are already in the program, they just have to be intentionally accessed. You
#       access these "standard libraries" with the 'import' command:

print(f'''
    Random Number Generator:

def make_random(modulus, a, c, seed):
    while True:
        seed = (a * seed + c) % modulus
        yield seed
      
generator = make_random(modulus = 2**32, a = 1103515245, c = 12345, seed = 1)
      
random_number = make_random(generator)
''')

print('====================================== \n')

#   You don't need to understand how this works, because frankly I don't either,
#       but this is a means of generating a random number in python, similar to
#       JavaScript's Math.random(). However, vanilla python doesn't actually have
#       a native way to create a random number, hence this complicated workaround
#       that simulates a random number without even being truly random. That being
#       said, you can get random numbers in python through a standard library:

import random

random_number = random.random()

print(f'''
    Random Number with standard library:
      
import random
      
random_number = {random_number}
''')

#       The 'random' creates a new keyword called "random" (more how this works later),
#       that comes with its own set of methods:

print(f'range_1_to_10 = {random.randint(1, 10)} \n')

number_list = [1, 2, 3, 4, 5]
random.shuffle(number_list)
print('number_list = [1, 2, 3, 4, 5]')
print(f'random.shuffle(number_list) = {number_list} \n')

print(f'choice("Hello world") = {random.choice("Hello World")} ')
#       All of these methods aren't in base python, but are immediately accessible by
#       importing standard libraries. With how long python has been around and how 
#       commonly used it is, there's almost definitely a standard library that can help
#       with whatever project you're working on.

print('====================================== \n')

#   If you don't want to import a specific function rather than an entire library, you
#       can use the 'from' keyword. For example, there's a 'math' library with a whole
#       host of mathematics methods, but if you want to save memory, you can only import
#       a single method, like the square root method:

from math import sqrt

square_root_of_25 = sqrt(25)

print(f'''
from math import sqrt
      
square_root_of_25 = {square_root_of_25}
''')

#       You can also rename methods if you feel like the standard name is unclear or
#       too long by using the 'as' keyword:

from math import ceil as round_up

from math import floor as round_down

rounded_up = round_up(99.1)

rounded_down = round_down(100.3)

print(f'''
from math import ceil as round_up
      
from math import floor as round_down
      
round_up(99.1) = {rounded_up}

round_down(100.9) = {rounded_down}
''')