import os
import cls.utils as u
import pygame as pg

defaults = {
    "entity": "default",
    "size": (16, 22),
    "border": None,
    "speed": 2
}

class Entity(pg.sprite.Sprite):
    def __init__(self, **kwargs):
        pg.sprite.Sprite.__init__(self)
        self.config = u.validateDict(kwargs, defaults)

        image = pg.Surface(self.config["size"], pg.SRCALPHA)
        path = u.PATH["entities"] + self.config["entity"]
        for dirs in os.walk(path):
            for each in dirs[2]:
                if each.split(".")[1] == "png":
                    image = pg.image.load(dirs[0] + "\\" + each)

        self.frames = u.getFrames(image, self.config["size"])
        self.image = self.frames[0]
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)
        self.speed = self.config["speed"]

        if self.config["border"]:
            self.image = u.drawBorder(
                self.image,
                size = self.config["border"][0],
                color = self.config["border"][1]
            )
    def move(self, axis):
        x, y = axis

        self.rect.left += x
        self.rect.top += y
