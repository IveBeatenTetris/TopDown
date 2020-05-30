import cls.utils as u
import pygame as pg
from .scene import *
from .entity import Entity

defaults = {
    "size": (320, 240),
    "border": None
}

class Camera(pg.Surface):
    def __init__(self, **kwargs):
        self.config = u.validateDict(kwargs, defaults)
        pg.Surface.__init__(self, self.config["size"], pg.SRCALPHA)
    def record(self, object):
        if type(object) == Scene:
            for layer in object.tilemap.layers:
                self.blit(layer, (0, 0))
        elif type(object) == Entity:
            self.blit(object.image, object.rect.topleft)
