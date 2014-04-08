# -*- coding: utf-8 -*-

import game

def out(array):
    for x in range(0,4*4,4):
        q=array[x:x+4]
        print(q)
    print("\n")

###################################################

def make_command(func, *args):
    return {
            'func':func,
            'args':(args)
            }

###################################################

def getKey():
    q=raw_input()
    return q[0]

###################################################

g2048 = game.game2048()

out(g2048.arr)

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
        # print(func)
        # exit()
        arr=func['func'](*func['args'])
        out(arr)
    else: k=False

# print(DIRECTIONS[BY_ROW](1))


