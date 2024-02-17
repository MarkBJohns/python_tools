print('==============================================================')

print('INSTALLING LIBRARIES')

print('==============================================================')

#   Say you want quick way to reformat colors. Theres a simple library you can import called
#       colorsys.

import colorsys

#       The base code in the library only allows for conversion between rgb (red, blue, greeen)
#       and hsl (hue, saturation, lightness), leaving no way to convert from or into hex code. To
#       get around this, you can use the library methods as a base to create your own functions:

def rgb_hsl(r, g, b):
    '''
    Takes in the rgb values of a color and returns the hsl values.

    >>> rgb_hsl(255, 0, 0)
    (0.0, 100.0, 50.0)
    '''
    r /= 255.0
    g /= 255.0
    b /= 255.0
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    return (h * 360, s * 100, l * 100)

#       The default method returns the order as hls, while the color pickers I'm looking at use hsl.
#       In addition, if the method ran our doctest, it would return (0.0, 127.5, -1.007905138339921),
#       rather than a simple set of numbers you can plug into a color picker. Our updated function
#       changes the order of the values as well as converting them to match the hue to be the degree
#       on the color wheel, and the percentages of the saturation and lightness.

red_hsl = rgb_hsl(255, 0, 0)

green_hsl = rgb_hsl(0, 255, 0)

blue_hsl = rgb_hsl(0, 0, 255)

print(f'''
red_hsl = rgb_hsl(255, 0, 0)
    {red_hsl}

green_hsl = rgb_hsl(0, 255, 0)
    {green_hsl}

blue_hsl = rgb_hsl(0, 0, 255)
    {blue_hsl}
''')

print('====================================== \n')

#   You can then reverse engineer the function to take in and rgb value and return an hsl value:

def hsl_rgb(h, s, l):
    '''
    Takes in the hsl values of a color and returns the rgb values.

    >>> hsl_rgb(0.0, 100.0, 50.0)
    (255, 0, 0)
    '''
    h /= 360.0
    s /= 100.0
    l /= 100.0
    r, g, b = colorsys.hls_to_rgb(h, l, s)
    return (round(r * 255), round(g * 255), round(b * 255))

yellow_rgb = hsl_rgb(60.0, 100.0, 50.0)

pink_rgb = hsl_rgb(300.0, 100.0, 50.0)

teal_rgb = hsl_rgb(180.0, 100.0, 50.0)

print(f'''
yellow_rgb = hsl_rgb(60.0, 100.0, 50.0)
    {yellow_rgb}

pink_rgb = hsl_rgb(300.0, 100.0, 50.0)
    {pink_rgb}

teal_rgb = hsl_rgb(180.0, 100.0, 50.0)
    {teal_rgb}
''')

print('====================================== \n')

#   Then create a way to convert from either hsl or rgb to hexcode:

def rgb_hex(r, g, b):
    '''
    Takes in an rgb color value and returns a hex code.
    
    >>> rgb_hex(255, 0, 0)
    '#FF0000'
    '''
    return "#{:02X}{:02X}{:02X}".format(r, g, b)

purple_hex = rgb_hex(100, 0, 200)

orange_hex = rgb_hex(234, 67, 11)

def hsl_hex(h, s, l):
    '''
    Takes in an hsl color value and returns a hex code.
    
    >>> hsl_hex(29.0, 100.0, 21.0)
    '#6B3400'
    '''
    (r, g, b) = hsl_rgb(h, s, l)
    return rgb_hex(r, g, b)

brown_hex = hsl_hex(29.0, 100.0, 21.0)

sky_blue_hex = hsl_hex(196.0, 76.0, 67.0)

print(f'''
purple_hex = rgb_hex(100, 0, 200)
    {purple_hex}

orange_hex = rgb_hex(234, 67, 11)
    {orange_hex}

brown_hex = hsl_hex(29.0, 100.0, 21.0)
    {brown_hex}

sky_blue_hex = hsl_hex(196.0, 76.0, 67.0)
    {sky_blue_hex}
''')

print('====================================== \n')

#   And finally, functions that convert hexcode into rgb or hsl

def hex_rgb(hex_code):
    '''
    Takes in a hex color code and returns the rgb values.

    >>> hex_rgb('#FF0000')
    (255, 0, 0)
    '''
    r = int(hex_code[1:3], 16)
    g = int(hex_code[3:5], 16)
    b = int(hex_code[5:7], 16)
    return (r, g, b)

picante_rgb = hex_rgb('#8D3F2D')

smoke_green_rgb = hex_rgb('#A3BCA6')

def hex_hsl(hex_code):
    '''
    Takes in a hex color code and returns the hsl values.
    
    >>> hex_hsl('#FFFF32')
    (60.0, 100.0, 60.0)'''
    r = int(hex_code[1:3], 16)
    g = int(hex_code[3:5], 16)
    b = int(hex_code[5:7], 16)

    h, s, l = rgb_hsl(r, g, b)
    return float(round(h)), float(round(s)), float(round(l))

picante_hsl = hex_hsl('#8D3F2D')

smoke_green_hsl = hex_hsl('#A3BCA6')

print(f'''
picante_rgb = hex_rgb('#8D3F2D')
    {picante_rgb}

picante_hsl = hex_hsl('#8D3F2D')
    {picante_hsl}

smoke_green_rgb = hex_rgb('#A3BCA6')
    {smoke_green_rgb}

smoke_green_hsl = hex_hsl('#A3BCA6')
    {smoke_green_hsl}
''')

#   And now you've taken base code from a standard library and created your own custom functions.
#       By simply using the import command, almost all of the actual work was done for you.

print('====================================== \n')

import webbrowser

browser = webbrowser.get('/usr/bin/firefox')

print('''
Welcome to the slowest websearch in the world!
''')
search_term = input("What are you looking for? \n ")

url = f'https://www.google.com/search?client=firefox-b-1-d&q={search_term}'

browser.open_new(url)

#   Here we have the webbrowser library that lets us access browser information, such as opening
#       a Google search with a dynamically entered search term. If we played with it more we
#       could create even more specific parameters or even enter forms from the terminal before using
#       that data online.