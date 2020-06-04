import pygame as pg
from cls.window import *
from cls.scene import *
from cls.camera import *
from cls.entity import *

app = Window(
    size = (800, 500),
    #resizable = True
)
scene = Scene(
    tilemap =  "test_ruin_001",
    tileset = "test_ruin1"
)
camera = Camera(
    size = scene.rect.size,
    border = (1, (200, 50, 25))
)
char = Entity(
    border = (1, (0, 100, 255))
)
def main():
    app.resize(scene.rect.size)
    char.rect.center = camera.rect.center
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
        #app.draw(char.image)
        camera.record(scene)
        camera.record(char)
        app.draw(camera)
        # ------------------------------ custom ------------------------------ #
        # events
        app.events
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            char.move((0, -char.speed))
        elif keys[pg.K_s]:
            char.move((0, char.speed))
        if keys[pg.K_a]:
            char.move((-char.speed, 0))
        elif keys[pg.K_d]:
            char.move((char.speed, 0))
        # drawing
        # updating
        app.update()

if __name__ == '__main__':
    main()
