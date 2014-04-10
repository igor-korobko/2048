# -*- coding: utf-8 -*-
import random

BY_ROW = 1
BY_COLUMN = 2
DIRECTIONS = {BY_ROW: lambda row: slice(row * 4, row * 4 + 4),
              BY_COLUMN: lambda col: slice(col, 4 * 4, 4)
              }


class Game2048:

    arr = [0]*(4*4)
    inv = False

    def __init__(self, array=0):
        if array != 0:
            self.arr = array
            print(array)
        else:
            self.add_new_elem(2)

    def invert_arr(self, array):
        return array[::-1]

    def shift(self, array):
        if self.inv:
            array = self.invert_arr(array)
        t_array = []
        box = 0
        for x in array:
            if x == 0:
                continue
            if x != box:
                if box:
                    t_array.append(box)
                box = x
            else:
                t_array.append(box*2)
                box = 0
        t_array.append(box)
        t_array += [0] * (4 - len(t_array))
        if self.inv:
            t_array = self.invert_arr(t_array)
        return t_array

    def add_new_elem(self, count_new_elem=1, clear_before_add=False):

        if clear_before_add:
            self.arr = [0] * (4 * 4)

        sample = random.sample(filter(lambda x:x[1] == 0, enumerate(self.arr)), count_new_elem)
        for cell in sample:
            self.arr[cell[0]] = 2
        return self.arr

    def work(self, direct, invert=False):
        self.inv = invert
        for x in range(0, 4):
            self.arr[DIRECTIONS[direct](x)] = self.shift(self.arr[DIRECTIONS[direct](x)])
        self.add_new_elem(1)
        return self.arr
