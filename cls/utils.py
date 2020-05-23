# dependencies
import pygame as pg
import ctypes, re, os, json
import xml.etree.ElementTree as et

# rules for json parsing
json_comments =  re.compile(
    "(^)?[^\S\n]*/(?:\*(.*?)\*/[^\S\n]*|/[^\n]*)($)?",
    re.DOTALL | re.MULTILINE
)

# path related
PATH = {
    "root": os.getcwd(),
    "assets": os.getcwd() + "\\assets\\",
    "tilemaps": os.getcwd() + "\\assets\\tilemaps\\",
    "tilesets": os.getcwd() + "\\assets\\tilesets\\"
}

# files & directories
def loadJSON(path):# dict
    """loads and converts a JSON file into a dict."""
    with open(path) as text:
        content = "".join(text.readlines())
        # looking for comments
        match = json_comments.search(content)
        while match:
            # single line comment
            content = content[:match.start()] + content[match.end():]
            match = json_comments.search(content)
        js = json.loads(content)
        if "name" in js:
            name = js["name"]
        else:
            name = path.split("\\")[-2]
        js.update({"name": name})
        js.update({"path": path})
        # //TODO tidy up
        s = path.split("\\")
        s = os.path.join(*s, "\\", *s[1:-1])
        js.update({"filepath": s})
        js.update({"filename": path.split("\\")[-1]})

    return js
def loadXML(path):
    """
    returns a 'xml.etree.ElementTree.ElementTree' object read from a xml file
        or object-type.
    """
    return et.parse(path)

# helper functions
def getDisplay(size, resizable=False):# pg.display.surface
    """
    creates a new window display and returns it. customisation possible.
    usage: screen = getDisplay(((1920, 1080), True)
    """
    if resizable is True:
        display = pg.display.set_mode(size, pg.RESIZABLE)
    else:
        display = pg.display.set_mode(size)

    return display
def getResolution():# tuple
    """returns full-screen size in a tuple."""
    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
    size = (user32.GetSystemMetrics(0), user32.GetSystemMetrics(1))

    return size
def validateDict(config={}, defaults={}):# dict
    """
    validates a dictionary by comparing it to the default values from another
    given dict.
    """
    validated = {}

    for each in defaults:
        try:
            validated[each] = config[each]
        except KeyError:
            validated[each] = defaults[each]

    return validated
