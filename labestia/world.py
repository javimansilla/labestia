import random

from labestia import settings as cfg
from labestia.board import Board
from labestia.characters import Warrior, Beast
from labestia.sounds import Sound


class World:

    def __init__(self):
        self.sound = Sound()
        self.board = Board()
        self.window = self.board.window
        self.warrior = Warrior()
        self.beast = Beast()

    def mainloop(self):
        self.window.listen()
        self.window.onkey(self.start_game, 'Return')
        self.window.onkey(self.exit, 'Escape')
        self.window.mainloop()

    def exit(self):
        self.window.bye()

    def start_game(self):
        print('start')
        self.sound.start()
        self.step_count = 0
        self.board.reset()
        self._health = cfg.WINNING / 2
        self.board.power.update_mark(self._health)
        self.reset_characters()
        self.window.listen()
        self.window.onkey(lambda: self.move_warrior(0, 1), 'Up')
        self.window.onkey(lambda: self.move_warrior(-1, 0), 'Left')
        self.window.onkey(lambda: self.move_warrior(0, -1), 'Down')
        self.window.onkey(lambda: self.move_warrior(1, 0), 'Right')
        self.move_beast(joke_prob=1)

    def reset_characters(self):
        self.warrior.up()
        self.warrior.goto(0, 0)
        self.warrior.down()
        self.warrior.clear()
        self.beast.turn('left')

    def update_health(self, delta):
        self._health += delta
        if self._health < 0:
            self._health = 0
        elif self._health > cfg.WINNING:
            self._health = cfg.WINNING
        self.board.power.update_mark(self._health)

        if self._health <= 0:
            self.game_over()
        elif self._health >= cfg.WINNING:
            self.you_won()

    def stop(self):
        self.sound.stop()
        for k in ['Up', 'Down', 'Left', 'Right']:
            self.window.onkey(None, k)

    def game_over(self):
        self.stop()
        self.board.message("Lo lamento, perdiste.")
        self.sound.play('losing')

    def you_won(self):
        self.stop()
        self.board.message("Felicitaciones!\nGanaste en %i pasos" % self.step_count)
        self.sound.play('winning')

    def move_warrior(self, dx, dy):
        x, y = self.warrior.position()

        if abs(x) == cfg.GRID_MAX and (dx * x) > 0:
            self.hit_wall()
            return
        if abs(y) == cfg.GRID_MAX and (dy * y) > 0:
            self.hit_wall()
            return

        if dx > 0:
            self.warrior.turn('right')
        elif dx < 0:
            self.warrior.turn('left')
        x2 = x + dx * cfg.GRID_SIZE
        y2 = y + dy * cfg.GRID_SIZE
        self.warrior.goto(x2, y2)
        self.count_step()

    def move_beast(self, joke_prob=None):
        x, y = self.beast.where_to_go(self.warrior)
        self.beast.move(x, y)
        if joke_prob is None:
            joke_prob = random.random()
        if joke_prob > 0.75:
            self.sound.play('seeyou')

    def hit_wall(self):
        self.sound.play('wall')

    def count_step(self):
        self.sound.play('step')
        self.step_count += 1
        if self.warrior.position() == self.beast.position():
            self.update_health(cfg.HUNT_PRICE)
            self.beast.turn('mad')
            self.sound.play('hunted')
            self.move_beast(joke_prob=0)
            self.beast.turn('mad')
            self.window.ontimer(lambda: self.beast.turn('right'), 700)
        else:
            self.update_health(-cfg.STEP_EFFORT)
            if random.random() < cfg.BEAST_SENSIBILITY:
                self.move_beast()
