# -*- coding: utf-8 -*-

import game
import printer

def make_command(func, *args):
    return {
            'func':func,
            'args':args
            }

def getKey():
    q=raw_input()
    return q[0]

if __name__=='main':
    g2048 = game.game2048()

    prin = printer.printer()
    prin.out(g2048.arr)

    event_map = {
            'w': make_command(g2048.work, g2048.BY_COLUMN, False),
            'a': make_command(g2048.work, g2048.BY_ROW, False),
            's': make_command(g2048.work, g2048.BY_COLUMN, True),
            'd': make_command(g2048.work, g2048.BY_ROW, True),
            'n': make_command(g2048.add_new_elem, 2, True),
        }

    k=True
    while k:
        k=getKey()
        if k in event_map:
            func=event_map[k]
            arr=func['func'](*func['args'])
            prin.out(arr)
        else: k=False




