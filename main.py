import pygame as pg
from cls.window import *

app = Window(
    size = (800, 500),
    resizable = True
)
def main():
    while True:
        # ------------------------------ custom ------------------------------ #
        print(app.rect)
        # ------------------------------ custom ------------------------------ #
        # events
        app.events
        # updating
        app.update()

if __name__ == '__main__':
    main()
