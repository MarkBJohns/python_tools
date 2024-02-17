print('==============================================================')

print('VIRTUAL ENVIRONMENTS')

print('==============================================================')

#   While it's generally useful to have a python package installed somewhere be accessible 
#       everywhere, there are some cases where this can get messy, and you want it to be localized
#       to one degree or another. For example, if a library is getting regular updates, there's a 
#       chance that an aspect of the library your project has been relying on can change in a way that
#       fundamentally breaks your code. Other reason to have your packages separated include:

#           1). You may not need the package for every project
#           2). You may want to better keep track of the specific libraries used for that particular
#               project (especially for group projects)
#           3). You may want a specific version of a package that could otherwise change

#       To make sure your packages stay localized to your project, you can create what's called a virtual
#       environment:

print("python3 -m venv venv")

#   What this line does is create a folder called "venv" with the venv module. This folder will already
#       have some files in it, but don't worry about those just yet, other than to notice one of them is
#       called "bin". The follow up to creating the venv folder is to run a command to enter the folder on
#       your terminal in a way that allows you to set things up:

print("source venv/bin/activate")

#       Upon entering this, you'll see that the prompt line on your terminal now begins with "(venv)",
#       indication the virtual environment. This command will also be entered quite often, as this is the 
#       way that you can reenter your virtual environment any time you leave it (usually by closing the
#       terminal window).

print('====================================== ')

#   While in a virtual environment, you're tied to the version of python you were using when the environment
#       was created, and you have access to the standard library, but you don't have access to anything you
#       globally installed with pip. So while you downloaded pypokedex in earlier notes, you can't access it
#       inside the virtual environment.

print(f'''
import pypokedex

absol = pypokedex.get(dex=359)
''')

#       If the above were actual code and I tried to run this file in my terminal, it would work outside of
#       the virtual environment, but while inside it, the attempt to run the file would return:

print(f'''
Traceback (most recent call last):
  File "/home/markbjohns/python/python_tools/virtual_environments.py", line 42, in <module>
    import pypokedex
ModuleNotFoundError: No module named 'pypokedex'
''')

#   While on the surface this seems like a hinderance, it can be useful for the reasons mentioned at the top
#       of these notes, as well as for different companies relying on specific versions of programs.

print('====================================== ')

#   To install a module into your virtual environment is the same as installing it globally, via the pip
#       command. There's a popular module called 'Faker' for example, that generates fake data so you can
#       test your code.

print("pip3 install Faker\n")

#       Now we can import it and change some method names around to make the coding easier:

from faker import Faker
fake = Faker() # This is from a Class, which we'll talk about later

fake_users = [{'name': fake.name(), 'address': fake.address()} for _ in range(5)]

print(f'''
from faker import Faker
fake = Faker()
      
fake_users = [{{'name': fake.name(), 'address': fake.address()}} for _ in range(5)]
      
fake_users =
{fake_users}
''')

#       But more importantly to these notes, this faker module only works in the virtual environment
#       created in this directory. If you enter "deactivate" in your shell, it will leave the virtual
#       environment and return to the global python interpreter. Try to run this file again and instead
#       of getting a list of random fake data, you'll get a ModuleNotFoundError, because faker was not
#       downloaded globally. Reenter "source venv/bin/activate" to enter the virtual environment again,
#       and running the file will once again return the data.

print('====================================== ')

#	If you ever need to see a list of which libraries are in your virtual environment, you can use the
#		"freeze" command:

print("pip3 freeze")

#		Which in this specific instance will return:

print(f'''
contourpy==1.2.0
cycler==0.12.1
Faker==23.2.0
fonttools==4.49.0
kiwisolver==1.4.5
matplotlib==3.8.3
mondrian-art==0.1.2
numpy==1.26.4
packaging==23.2
pillow==10.2.0
pyparsing==3.1.1
python-dateutil==2.8.2
six==1.16.0
''')

#	This tells you both the imported libraries that are in your virtual environment, as well as the specific
#		version of the library that's being used. It's good to have a list so that any colaborators can know
#		what they need to have the program work on their computers, but in a way where the libraries aren't 
#		downloaded into the files, making the project size dramatically bigger and harder to share/download.

#	It's also useful to see what additonal libraries are part of the libraries you import. For example, the only
#		libraries I directly downloaded were Faker and mondrian-art, but several other libraries got imported as
#		the ones we imported directly need them to run.

#	The standard way to store which libraries are needed for the project is by saving them to a text file,
#		usually called "requirements":

print("pip3 freeze > requirements.txt")

#	This is particularly useful, because the venv file is typically not added to repositories. This is because
#		the file is extremely large and full of code that you didn't write, so you don't want to take the time and
#		file space needed to upload a large, unnecessary file. You can get around this by creating a .gitignore
#		file and putting venv in it:

print("touch .gitignore")

print('====================================== \n')

