# -*- coding: utf-8 -*-

from game import Game2048, BY_COLUMN, BY_ROW
from printer import Printer
from db import DB


def key_gen():
#     генератор ключа......
#   return key
    pass


def make_command(func, *args):
    return {'func': func,
            'args': args
            }


def get_key():
    q = raw_input()
    return q[0]


def what_do():
#   спрашивает следить за кем то или
#
#     if action == 1 #начать новую игру
#         # ....
#
#     if action == 2 #продолжить
#         # ....
#
#     if action == 3 #следить
#         # ....
#  ну или как-то по другому
    pass


if __name__ == '__main__':

    some_value = what_do()
    #..............
     db = DB()
   # .............
    g2048 = Game2048()# сюда передавать массив из базы
    print_ = Printer()


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

