# -*- coding: utf-8 -*-
import random

class game2048:

    arr=[]
    BY_ROW = 1
    BY_COLUMN = 2
    DIRECTIONS={
        BY_ROW:lambda row:slice(row*4,row*4+4),
        BY_COLUMN:lambda col:slice(col,4*4,4)
    }
    inv=False

    def __init__(self):
        self.arr = [0]*(4*4)
        self.add_new_elem(2)

    def invertArr(self,array):
        return array[::-1]

    def shift(self,array):
        if self.inv:
            array=self.invertArr(array)
        t_array=[]
        box = 0
        for x in array:
            if x==0:
                continue
            if x != box:
                if box:
                    t_array.append(box)
                box = x
            else:
                t_array.append(box*2)
                box = 0
        t_array.append(box)
        t_array+=[0]*(4-len(t_array))
        if self.inv:
            t_array=self.invertArr(t_array)
        return t_array

    def add_new_elem(self,countNewElem=1,clearBeforeAdd=False):

        if(clearBeforeAdd):
            self.arr=[0]*(4*4)

        sample = random.sample(filter(lambda x:x[1]==0,enumerate(self.arr)),countNewElem)
        for cell in sample:
            self.arr[cell[0]] = 2
        return self.arr

    def work(self,dir,invert=False):
        self.inv=invert
        for x in range(0,4):
            self.arr[self.DIRECTIONS[dir](x)]=self.shift(self.arr[self.DIRECTIONS[dir](x)])
        self.add_new_elem(1)
        return self.arr

