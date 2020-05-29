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
    "tilesets": os.getcwd() + "\\assets\\tilesets\\",
    "entities": os.getcwd() + "\\assets\\entities\\"
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
def createTiledMap(config, tiles):# dict
    """
    drawing tiles on a pygame surface and returning it in a dict together with
    a list of wall rects and other special blocks with their position.
    """
    tilesize = tiles[0].image.get_rect().size

    blocks = []
    surface = pg.Surface(
        (
            config["width"] * tilesize[0],
            config["height"] * tilesize[1]
        ),
        pg.SRCALPHA)
    playerstart = None

    i = 0
    for row in range(config["height"]):
        y = row * tilesize[1]
        for line in range(config["width"]):
            x = line * tilesize[0]

            # only draw tile if area isn't empty
            if config["data"][i] != 0:
                tile = tiles[config["data"][i] - 1]
                rect = pg.Rect((x, y), tile.image.get_rect().size)
                # only draw if the tile is visible
                if tile.visible is True:
                    surface.blit(tile.image, (x, y))
                # add a block rect to blocklist if tile is not passable
                if tile.block:
                    blocks.append(rect)

                # set player-start position if there is a tile placed for that
                if tile.name:
                    if tile.name == "player_start":
                        playerstart = rect

            i += 1

    return {
        "image": surface,
        "blocks": blocks,
        "player_start": playerstart
    }
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
def getFrames(image, framesize):# list
    """
    return a list of frames clipped from an image.
    'framesize' must be a tuple of 2.
    usage:
    frames = getFrames(spritesheet, (16, 16)).
    """
    frames = []

    rows = int(image.get_rect().height / framesize[1])
    cells = int(image.get_rect().width / framesize[0])
    rect = pg.Rect((0, 0), framesize)

    # running each frame
    for row in range(rows):
        y = row * framesize[1]
        rect.top = y
        for cell in range(cells):
            x = cell * framesize[0]
            rect.left = x

            image.set_clip(rect)
            clip = image.subsurface(image.get_clip())

            frames.append(clip)
    del(clip, rect)

    return frames
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
