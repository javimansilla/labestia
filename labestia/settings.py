import os.path


GRID_SIZE = 65
GRID_SPAN = 3
GRID_MAX = GRID_SIZE * GRID_SPAN

HUNT_PRICE = 100
STEP_EFFORT = 15
WINNING = 360
BEAST_SENSIBILITY = 0.25

dir_path = os.path.dirname(os.path.realpath(__file__))
SOUNDS_PATH = os.path.join(dir_path, 'assets', 'audio')
IMGS_PATH = os.path.join(dir_path, 'assets', 'img')
