#import pygame as pg
from cls.window import *
from cls.scene import *
from cls.entity import *

app = Window(
    size = (800, 500),
    resizable = True
)
scene = Scene(
    tilemap =  "test_ruin_001",
    tileset = "test_ruin1"
)
char = Entity(

)
def main():
    while True:
        # ------------------------------ custom ------------------------------ #
        #print(app.rect)
        #app.draw(scene.tileset)
        #app.draw(scene.tileset.tiles[2].image)
        #app.draw(scene.tilemap)
        #app.draw(scene.tilemap.layers[0])
        #app.draw(scene.tilemap.layers[1])
        #for layer in scene.tilemap.layers:
            #app.draw(layer)
        app.draw(char.image)
        # ------------------------------ custom ------------------------------ #
        # events
        app.events
        # drawing
        # updating
        app.update()

if __name__ == '__main__':
    main()
