# -*- coding: utf-8 -*-

from game import Game2048, BY_COLUMN, BY_ROW
from printer import Printer
from db import DB, Subscribe
from optparse import OptionParser
import random


def key_gen():
    return random.randint(1, 1000)


def make_command(func, *args):
    return {'func': func,
            'args': args
            }


def get_key():
    q = raw_input()
    return q[0]


def what_do():
    parser = OptionParser(usage="python index_.py -k int (access key) "
                                # "\n -n 1 or 0 (new game true or false) "
                                "\n -c int (key for continue)")
    parser.add_option("-k", type="int", dest="watch", default="0")
    parser.add_option("-s", type="string", dest="server", default="localhost")
    parser.add_option("-c", type="int", dest="play", default="0")
    (options, args) = parser.parse_args()

    if options.play != 0:
        return make_command(play, options.play)

    elif options.watch != 0:
        return make_command(watch, options.watch, options.server)

    else:
        return make_command(play, 0)


def play(key):
    print(key)
    user_key = key

    db = DB()
    arr = 0

    if user_key != 0:
        arr = db.get(user_key)
    else:
        user_key = key_gen()

    g2048 = Game2048(arr)
    print("user_key:"+user_key.__str__())

    print_ = Printer()
    print_.out(g2048.arr)

    event_map = {'w': make_command(g2048.work, BY_COLUMN, False),
                 'a': make_command(g2048.work, BY_ROW, False),
                 's': make_command(g2048.work, BY_COLUMN, True),
                 'd': make_command(g2048.work, BY_ROW, True),
                 'n': make_command(g2048.add_new_elem, 2, True),
                 'm': make_command(db.save, arr, user_key)
                 }

    k = True
    while k:
        k = get_key()
        if k in event_map:
            func = event_map[k]
            arr = func['func'](*func['args'])
            db.publish(arr, user_key)
            print_.out(arr)
        else:
            k = False


def watch(key, server):

    print_ = Printer()
    k = str(key)
    subscr = Subscribe(server)

    while 1:
        array = subscr.subscribe(k)
        print_.out(array)


# -------------------------------------------------------
if __name__ == '__main__':
    action = what_do()
    action["func"](*action["args"])
