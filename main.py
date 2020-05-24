#import pygame as pg
from cls.window import *
from cls.scene import *

app = Window(
    size = (800, 500),
    resizable = True
)
scene = Scene(
    tilemap =  "test_ruin_001",
    tileset = "test_ruin1"
)
def main():
    while True:
        # ------------------------------ custom ------------------------------ #
        #print(app.rect)
        #app.draw(scene.tileset)
        #app.draw(scene.tileset.tiles[2].image)
        app.draw(scene.tilemap)
        #app.draw(scene.tilemap.layers[0])
        # ------------------------------ custom ------------------------------ #
        # events
        app.events
        # drawing
        # updating
        app.update()

if __name__ == '__main__':
    main()
