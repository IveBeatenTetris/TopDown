import os
import cls.utils as u
import pygame as pg

defaults = {
    "scene": {
        "tilemap": "test_ruin_001",
        "tileset": "default"
    },
    "tile": {
		"name": "Unnamed",
		"block": False,
		"visible": True
    }
}

class Scene(object):
    def __init__(self, **kwargs):
        self.cfg = u.validateDict(kwargs, defaults["scene"])
        self.tileset = Tileset(self.cfg["tileset"])
        self.tilemap = Tilemap(self.cfg["tilemap"], self.tileset)
        self.rect = self.tilemap.layers[0].get_rect()
class Tilemap(pg.Surface):
    def __init__(self, name, tileset):
        self.cfg = self.loadTileMap(name)
        pg.Surface.__init__(self, self.cfg["size"], pg.SRCALPHA)
        self.tileset = tileset
        self.layers = self.createLayers()
    def createLayers(self):# list
        row_length = int(self.cfg["size"][1] / self.cfg["tilesize"][1])
        col_length = int(self.cfg["size"][0] / self.cfg["tilesize"][0])
        layer = pg.Surface(self.cfg["size"])
        layers = []

        for l in self.cfg["layers"]:
            i = 0
            for row in range(row_length):
                y = self.cfg["tilesize"][0] * row
                for col in range(col_length):
                    x = self.cfg["tilesize"][1] * col

                    data = l["data"][i]
                    self.blit(self.tileset.tiles[data-1].image, (x, y))
                    layer.blit(self.tileset.tiles[data-1].image, (x, y))

                    i += 1

            layers.append(layer)

        return layers
    def loadTileMap(self, name):# dict
        path = u.PATH["tilemaps"] + name + "\\"
        cfg = {
            "layers": []
        }

        for dirs in os.walk(path):
            for each in dirs[2]:
                if each.split(".")[1] == "tmx":
                    config = u.loadXML(dirs[0] + "\\" + each)

        root = config.getroot()
        cfg["tilesize"] = (
            int(root.attrib["tilewidth"]),
            int(root.attrib["tileheight"])
        )
        cfg["size"] = (
            int(root.attrib["width"]) * cfg["tilesize"][0],
            int(root.attrib["height"]) * cfg["tilesize"][1]
        )
        for child in root:
            if child.tag == "tileset":
                path = u.PATH["assets"] + child.attrib["source"].split("../")[-1]
                cfg["tileset"] = path
            elif child.tag == "layer":
                layer = {
                    "id": child.attrib["id"],
                    "name": child.attrib["name"],
                    "size": (
                        int(child.attrib["width"]),
                        int(child.attrib["height"])
                    )
                }
                for each in child:
                    if each.tag == "data":
                        numbers = each.text.split(",")
                        for i in range(len(numbers)):
                            numbers[i] = int(numbers[i])
                        layer.update({"data": numbers})

                cfg["layers"].append(layer)
        return cfg
class Tileset(pg.Surface):
    def __init__(self, name):
        self.cfg = self.loadTileSet(name)
        self.image = pg.image.load(self.cfg["image"])
        pg.Surface.__init__(self, self.cfg["size"])
        self.tiles = self.createTiles()
        self.blit(self.image, (0, 0))
    def createTiles(self):# list
        tiles = []
        size = (
            int(self.cfg["size"][0] / self.cfg["tilesize"][0]),
            int(self.cfg["size"][1] / self.cfg["tilesize"][1])
        )

        i = 0
        for row in range(size[1]):
            y = row * self.cfg["tilesize"][1]
            for col in range(size[0]):
                x = col * self.cfg["tilesize"][0]

                config = {}
                image = pg.Surface(self.cfg["tilesize"], pg.SRCALPHA)
                image.blit(self.image, (-x, -y))
                config["image"] = image
                config["id"] = i

                tiles.append(Tile(config))

            i += 1

        return tiles
    def loadTileSet(self, name):# dict
        path = u.PATH["tilesets"] + name + "\\"
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
class Tile(pg.sprite.Sprite):
    def __init__(self, config):
        pg.sprite.Sprite.__init__(self)
        self.id = config["id"]
        self.image = config["image"]
        self.rect = self.image.get_rect()
