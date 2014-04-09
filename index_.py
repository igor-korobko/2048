# -*- coding: utf-8 -*-

from game import Game2048, BY_COLUMN, BY_ROW
from printer import Printer
from db import DB


def make_command(func, *args):
    return {'func': func,
            'args': args
            }


def get_key():
    q = raw_input()
    return q[0]


if __name__ == '__main__':

    g2048 = Game2048()
    print_ = Printer()
    db = DB()

    print_.out(g2048.arr)

    event_map = {'w': make_command(g2048.work, BY_COLUMN, False),
                 'a': make_command(g2048.work, BY_ROW, False),
                 's': make_command(g2048.work, BY_COLUMN, True),
                 'd': make_command(g2048.work, BY_ROW, True),
                 'n': make_command(g2048.add_new_elem, 2, True)
                 }

    k = True
    while k:
        k = get_key()
        if k in event_map:
            func = event_map[k]
            arr = func['func'](*func['args'])
            print_.out(arr)
        else:
            k = False

