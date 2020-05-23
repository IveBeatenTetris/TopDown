import os
import cls.utils as u
import pygame as pg

defaults = {
    "map": {
        #"tilemap": "test_ruin_001",
        "tileset": "default"
    }
}

def loadTileSet(path):
    path = u.PATH["tilesets"] + path + "\\"
    cfg = {}

    for dirs in os.walk(path):
        for each in dirs[2]:
            if each.split(".")[1] == "tsx":
                config = u.loadXML(dirs[0] + "\\" + each)
                continue

    root = config.getroot()
    cfg["name"] = root.attrib["name"]
    cfg["tilesize"] = (
        int(root.attrib["tilewidth"]),
        int(root.attrib["tileheight"])
    )
    cfg["tilecount"] = root.attrib["tilecount"]
    for child in root:
        if child.tag == "image":
            cfg["image"] = path + "\\" + child.attrib["source"]
            cfg["size"] = (
                int(child.attrib["width"]),
                int(child.attrib["height"])
            )

    return cfg

class Map(object):
    def __init__(self, **kwargs):
        self.cfg = u.validateDict(kwargs, defaults["map"])
        self.tileset = Tileset(self.cfg["tileset"])
class Tileset(pg.Surface):
    def __init__(self, name):
        self.cfg = loadTileSet(name)
        pg.Surface.__init__(self, self.cfg["size"])
        self.blit(pg.image.load(self.cfg["image"]), (0, 0))
