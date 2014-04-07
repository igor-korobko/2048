
import random

def out(array):
        # print(array)
        for x in range(0,4*4,4):
            q=array[x:x+4]
            print(q)


class manage:

    array=[]

    def __init__(self):
        map=Init()
        self.array=map.new_game(2)
        del map

    def run(self):
        i=0
        obj=0
        out(self.array)
        newGameFlag=False
        while i<99:
            c=raw_input()
            k=ord(c)

            if k == 119:
                obj = Up(self.array)


            if k==110:
                newGameFlag=True
                break

            if obj!=0:
                i+=1
                obj.move()
                self.array=obj.add_new_elem(1)
                out(self.array)

        if newGameFlag:
            print("new game")
            self.__init__()
            self.run()

###################################################

class Init:
    arr=[]

    def new_game(self,countNewElem = 2):

        i=0

        while i<countNewElem:
            col=random.randint(0,4*4-1)
            if self.arr[col] == 0:
               self.arr[col] = 2
               i+=1
        return self.arr

    def get_array(self):
        return self.arr

    def __init__(self):
         self.arr=[0]*(4*4)


##################################################

class All():

    arr=[]
    arrFlags=[]

    def __init__(self,t_array):
        self.arr = t_array

    def add_new_elem(self,countNewElem=1):
        i=0
        while i<countNewElem:
            col=random.randint(0,4*4-1)
            if self.arr[col] == 0:
               self.arr[col] = 2
               i+=1
        return self.arr

    def do_it(self,array):
        t_array=[]
        for x in array:
            if x>0:
                l=len(t_array)
                if l>0:
                    if t_array[l-1]==x:
                        t_array[l-1]+=x
                    else:
                        t_array.append(x)
                else:
                    t_array.append(x)

        t_array+=[0]*(4-len(t_array))
        return t_array
###################################################

class Up(All):

    def move(self):

        for x in range(0,4):
            tmp=self.do_it(self.arr[x::4])
            self.arr[x::4]=tmp

        return self.arr



m=manage()
m.run()