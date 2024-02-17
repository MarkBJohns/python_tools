print('DOCSTRINGS AND DOCTESTS')

print('==============================================================')

#   You've already seen docstrings at this point, there an undeclared string value
#       coded directly after a function gets declared:

def add_up_to_four_nums(a, b, c=0, d=0):
    '''
    Takes up to 4 numbers and returns the sum of all of them.
    
    It must take at least 2 numbers, but the 3rd and 4th numbers
    are defaulted to 0 to allow for fewer than 4.'''
    return a + b + c + d

#       As this is not a typical x + y addition function and can take in a dynamic
#       amount of parameters, it's useful to have a description of what the function
#       can do, so the user understands why and how to use it. To access the
#       docstring, you can use the built in 'help()' method:

print('help(add_up_to_four_nums)')

print(f'''
Help on function add_up_to_four_nums in module --main--:
      
add_up_to_four_nums(a, b, c=0, d=0)
    Takes up to 4 numbers and returns the sum of all of them.
      
    It must take at least 2 numbers, but the 3rd and 4th numbers
    are defaulted to 0 to allow for fewer than 4.
''')

print('====================================== \n')

#   In addition to a docstring, you can also create something called a doctest, which
#       are function calls in the docstring with the expected outcome. For example, we'd
#       expect add_up_to_four_nums(1, 2, 3, 4) to equal 10, (1, 2, 3) to equal 6, and
#       (1, 2) to equal 3. There's a specific syntax you can use from within a docstring
#       to implement this check:

quotes = '"""'
print(f'''
    Doctest example:
      
def add_up_to_four_nums(a, b, c=0, d=0):
    {quotes}docstring example docstring example docstring
        >>> add_up_to_four_nums(1, 2, 3, 4)
        10
      
        >>> add_up_to_four_nums(1, 2, 3)
        6
      
        >>> add_up_to_four_nums(1, 2)
        3
    {quotes}
''')

#   To see it in action, here's a new, simple function

def multiply(x, y):
    '''
    Multiplies two values, x and y
    
    >>> multiply(2, 2)
    4
    
    >>> multiply(2, 0)
    0
    
    >>> multiply(1, 2)
    2
    '''
    return x * y

#       Given the doctests and their expected results, you can check to see that the
#       function is running as intended by using the doctest command in your terminal:

print(f'''
    Doctest running
      
python3 -m doctest your_file.py
''')

#       If your function works as intended, it will run the file normally. This is good,
#       however, as the doctest will only return some specific information should one of
#       your doctests return an unexpected result. If you do want to see more specific
#       information, you can add a -v for "verbose" to the command:


print(f'''
    Verbose doctest result
      
python3 -m doctest -v your_file.py
''')

#       This will run your file like normal, but at the end will print a message showing
#       what it tested, what the expected results were, and what the real results were.

print('====================================== \n')

funct_string = '''
    Substracts y from x
    
    >>> subtraction(10, 5)
    5

    >>> subtraction(5, 10)
    5
    '''

print(f'''
def subtraction(x, y):
    {funct_string}
    return x - y
''')

#   You should be able to see a clear issue here: 5 - 10 = -5, not 5. The function doesn't
#       do anything to account for the placement of the higher number, so you can return
#       negative nunbers. If you run a doctest, it will fail, and you'll get this response:

print(f'''
**********************************************************************
File "/home/markbjohns/python/python_tools/doctests.py", line 106, in doctests.subtraction
Failed example:
    subtraction(5, 10)
Expected:
    5
Got:
    -5
**********************************************************************
1 items had failures:
   1 of   2 in doctests.subtraction
***Test Failed*** 1 failures.
''')

#       If you want a subtraction function that avoids going into negative numbers, you can
#       include that except condition in you doctest with a keyword called Traceback:

print('====================================== \n')

def subtraction(x, y):
    """
    Subtracts y from x and returns the difference, so long as it does not result
    in a negative number.

    >>> subtraction(10, 5)
    5

    >>> subtraction(5, 5)
    0

    >>> subtraction(5, 10)
    Traceback (most recent call last):
    ...
    ValueError: Result cannot be less than 0, please be sure x > y
    """
    result = x - y
    if result < 0:
        raise ValueError("Result cannot be less than 0, please be sure x > y")
    return result

#       Now if you run a doctest in the terminal, even though one of the doctests
#       failed, it failed in a way we expected it to, so it passes the test.

#   Doctests are just parts of the docstring that don't take up processing memory and
#       won't actually run unless they are specifically called upon, but they can be
#       useful to ensure that your code works the way you want it to, collaborators can
#       see how code is supposed to work, and will be even more useful in OOP to clarify
#       what classes are designed to do.