print('==============================================================')

print('SHARING CODE BETWEEN FILES')

print('==============================================================')

#   In addition to importing code from a standard library, you can import your own code from 
#       another file. The syntax is identical, using the 'import', 'from' and/or 'as' commands:

import sharing_msg

#       On your shell, you'll see a message that isn't present anywhere in this file. It will
#       explain both why you're seeing the message, and how to resolve the issue of getting
#       more data than you actually want.

print('======================================')

#   To see this in action, if you run sharing_msg on your shell, it will say "Hello World!" This is
#       because it uses the conditional stated above to prevent the code that printed "Hello World!"
#       from spilling into this file:

print(f'''
message = "Hello World!"

def greeting():
    print(message)

if __name__ == "__main__":

    greeting()
''')

#       The call to run the greeting() function is placed in the conditional, so it doesn't run in
#       this file. But note that the function itself, as well as the variable that it's calling, are
#       not in the conditional. This means we have access to both of them in this file as well:

print("sharing_msg.greeting()")
sharing_msg.greeting()

#       But something to note is that even though we can access the 'message' variable from sharing_msg,
#       we cannot redeclare it:

message = "Goodbye Moon!"

print('\nmessage = "Goodbye Moon!"')
print("sharing_msg.greeting()")
sharing_msg.greeting()

print('====================================== \n')

#       The same process of importing specific functions or renaming them applies as well, as you can
#       see with this specific function from sharing_msg being renamed as something more intuitive:

from sharing_msg import jkljdslkjdsl as square

print('from sharing_msg import jkljdslkjdsl as square')
print('square(7)')
print(square(7))

print('====================================== \n')

#   Note that with the first example, you had to use the file name to call the function you imported,
#       or sharing_msg.greeting(), while for square() you didn't have to use the file name to call a
#       method. That's one of the benefits to renaming the functions as well:

from sharing_msg import greeting as greeting

print('from sharing_msg import greeting as greeting')
print('greeting()')
greeting()