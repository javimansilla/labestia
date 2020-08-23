import os.path

import pygame
from labestia import settings as cfg


def _path(*args):
    return os.path.join(cfg.SOUNDS_PATH, *args)


class Sound:

    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.music.load(_path('songs', 'happy.ogg'))
        pygame.mixer.music.set_volume(0.05)
        self.effects = {}

        for name in ['step', 'wall', 'hunted', 'seeyou', 'winning', 'losing']:
            self.effects[name] = pygame.mixer.Sound(_path(name + '.wav'))

    def stop(self):
        pygame.mixer.music.stop()

    def start(self):
        pygame.mixer.music.play(-1)

    def play(self, name):
        self.effects[name].play()
