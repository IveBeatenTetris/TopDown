import os
import cls.utils as u
import pygame as pg

defaults = {
    "entity": "default"
}

class Entity(pg.sprite.Sprite):
    def __init__(self, config={}):
        pg.sprite.Sprite.__init__(self)
        self.config = u.validateDict(config, defaults)

        self.image = pg.Surface((16, 32), pg.SRCALPHA)
        path = u.PATH["entities"] + self.config["entity"]
        for dirs in os.walk(path):
            for each in dirs[2]:
                if each.split(".")[1] == "png":
                    self.image = pg.image.load(dirs[0] + "\\" + each)

        #self.image = config["image"]
        self.rect = self.image.get_rect()
