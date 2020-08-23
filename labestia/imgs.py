import os.path
import turtle

from labestia import settings as cfg


def img_path(*args):
    return os.path.join(cfg.IMGS_PATH, *args)


def load_image(fname):
    fpath = img_path(fname)
    turtle.register_shape(fpath)
    return fpath
