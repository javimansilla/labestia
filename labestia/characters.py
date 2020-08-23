import random
import turtle

from labestia import settings as cfg
from labestia.imgs import load_image


class Sprite:

    def __init__(self):
        self.me = turtle.Turtle()
        self.shapes = {}

    def turn(self, where):
        self.me.shape(self.shapes[where])

    def __getattribute__(self, attr):
        try:
            # Default behaviour
            return object.__getattribute__(self, attr)
        except Exception as error:
            return object.__getattribute__(self.me, attr)


class Warrior(Sprite):

    def __init__(self):
        super().__init__()
        self.me.pensize(10)
        self.me.color('white')

        self.shapes = {
            'left': load_image('warrior_left.gif'),
            'right': load_image('warrior_right.gif')
        }
        self.turn('left')

    def turn(self, where):
        self.me.shape(self.shapes[where])


class Beast(Sprite):

    def __init__(self):
        super().__init__()
        self.me.up()

        self.shapes = {
            'left': load_image('beast_left.gif'),
            'right': load_image('beast_right.gif'),
            'mad': load_image('beast_mad.gif')
        }
        self.turn('left')

    def where_to_go(self, warrior):
        _x, _y = self.position()
        wx, wy = warrior.position()
        x, y = _x, _y
        while (x, y) in [(_x, _y), (wx, wy)]:
            x = random.randint(-cfg.GRID_SPAN, cfg.GRID_SPAN) * cfg.GRID_SIZE
            y = random.randint(-cfg.GRID_SPAN, cfg.GRID_SPAN) * cfg.GRID_SIZE
        return x, y

    def move(self, x, y):
        self.goto(x, y)
        if x < 0:
            self.turn('right')
        else:
            self.turn('left')
