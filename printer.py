# -*- coding: utf-8 -*-
class Printer:

    def out(self,array):
        for x in range(0,4*4,4):
            q=array[x:x+4]
            print('{0:{width}{base}} {1:{width}{base}} {2:{width}{base}} {3:{width}{base}}'.format(*q, base='d' , width=5))
