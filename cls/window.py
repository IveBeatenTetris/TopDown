import pygame as pg
import cls.utils as u
import sys, os

pg.init()
os.environ["SDL_VIDEO_CENTERED"] = "1"

defaults = {
    "resizable": False,
    "title": "TopDown 0.1",
    "size": u.getResolution(),
    "fps": 60
}

class Window(object):
    def __init__(self, **kwargs):
        self.cfg = u.validateDict(kwargs, defaults)
        self.display = u.getDisplay(self.cfg["size"], self.cfg["resizable"])
        pg.display.set_caption(self.cfg["title"])
        self.clock = pg.time.Clock()
    @property# list
    def events(self):
        events = pg.event.get()

        for evt in events:
            if (
                evt.type is pg.QUIT
                or evt.type is pg.KEYDOWN and evt.key is pg.K_ESCAPE
            ):
                pg.quit()
                sys.exit()
            if evt.type is pg.VIDEORESIZE:
                self.resize(evt.size)

        return events
    # dynamic attributes
    @property# int
    def fps(self):
        return int(self.clock.get_fps())
    @property# rect
    def rect(self):
        return self.display.get_rect()
    # class methodes
    def draw(self, obj, pos=(0, 0), rect=None):
        if rect:
            self.display.blit(obj, pos, rect)
        else:
            self.display.blit(obj, pos)
    def resize(self, size):
        self.display = u.getDisplay(size, self.cfg["resizable"])
    def update(self):
        pg.display.update()
        #self.display.fill((0, 0, 0))
        self.clock.tick(self.cfg["fps"])
        pg.display.set_caption(self.cfg["title"] + "          " + str(self.fps))
