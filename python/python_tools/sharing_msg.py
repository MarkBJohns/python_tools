#   IGNORE IF NOT READING SHARING_CODE_BETWEEN_FILES.PY

print(f'''
The reason you're seeing this is because 'import' takes in the entire file, including
    any printed statements, input commands, etc. The way you can get around this is
    with an important conditional:
      
    if __name__ == "__main__":
''')

message = "Hello World!"

def greeting():
    print(message)

def jkljdslkjdsl(x):
    return x * x

if __name__ == "__main__":

    greeting()