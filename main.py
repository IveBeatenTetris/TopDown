#import pygame as pg
from cls.window import *
from cls.map import *

app = Window(
    size = (800, 500),
    resizable = True
)
scene = Map(
    #tilemap =  "test_ruin_001",
    #tileset = "test_ruin1"
)
def main():
    while True:
        # ------------------------------ custom ------------------------------ #
        #print(app.rect)
        app.draw(scene.tileset)
        # ------------------------------ custom ------------------------------ #
        # events
        app.events
        # drawing
        # updating
        app.update()

if __name__ == '__main__':
    main()
