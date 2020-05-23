# dependencies
import pygame as pg
import ctypes, re, os, json

# path related
PATH = {
    "root": os.getcwd()
    #"maps": os.getcwd() + "\\maps\\",
}

#helper functions
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
