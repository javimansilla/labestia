import turtle

from labestia import settings as cfg
from labestia.imgs import load_image, img_path


class PowerBar:

    def __init__(self):
        self.bar = turtle.Turtle()
        self.bar.color('white')
        self.bar.shape(load_image('powerbar.gif'))
        self.bar.up()
        self.y = cfg.GRID_SIZE/2 + cfg.GRID_MAX
        self.bar.goto(0, self.y)

        self.mark = turtle.Turtle()
        self.mark.shape(load_image('heart.gif'))
        self.mark.up()
        self.mark.goto(0, self.y)

    def reset(self):
        self.mark.goto(0, self.y)
        self.bar.clear()

    def update_mark(self, level):
        # substract half MAX to center
        lvl = level - cfg.WINNING / 2
        self.mark.goto(lvl, self.y)


class Board:

    def __init__(self):
        turtle.speed(0)
        turtle.hideturtle()
        turtle.color('grey')
        turtle.width(7)
        window = turtle.Screen()
        window.setup(startx=600, width=601, height=538)
        turtle.bgcolor('grey')
        turtle.bgpic(img_path('background.png'))
        for i in range(-cfg.GRID_SPAN, cfg.GRID_SPAN+1):
            step_i = i * cfg.GRID_SIZE
            self.draw_line(-cfg.GRID_MAX, step_i, cfg.GRID_MAX, step_i)
            self.draw_line(step_i, -cfg.GRID_MAX, step_i, cfg.GRID_MAX)
        self.window = window
        self.power = PowerBar()

    def reset(self):
        self.power.reset()

    def message(self, msg):
        self.power.bar.write(
            msg, align="Center", font=("Arial", 30, "bold")
        )

    @staticmethod
    def draw_line(x1, y1, x2, y2):
        turtle.up()
        turtle.goto(x1, y1)
        turtle.down()
        turtle.goto(x2, y2)
