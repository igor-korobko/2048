import random

def out(array):
        for x in range(0,4*4,4):
            q=array[x:x+4]
            print(q)
        print("\n")

###################################################

def shift(array):

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

    return t_array

###################################################

def add_new_elem(arr,countNewElem=1,clearBeforeAdd=False):

    if(clearBeforeAdd):
        arr=[0]*(4*4)

    sample = random.sample(filter(lambda x:x[1]==0,enumerate(arr)),countNewElem)
    for cell in sample:
        arr[cell[0]] = 2
    return arr

##################################################

BY_ROW = 1
BY_COLUMN = 2
DIRECTIONS={
    BY_ROW:lambda row:slice(row*4,row*4+4),
    BY_COLUMN:lambda col:slice(col,4*4,4)
}
##################################################

def work(arr,dir,invert):
    for x in range(0,4):
        if invert:
            tmp=arr[DIRECTIONS[dir](x)]
            tmp=shift(tmp[::-1])
            arr[DIRECTIONS[dir](x)]=tmp[::-1]
        else:
            arr[DIRECTIONS[dir](x)]=shift(arr[DIRECTIONS[dir](x)])
    arr=add_new_elem(arr,1)
    return arr

##################################################

arr = [2,0,0,2,
       0,0,4,2,
       0,0,0,0,
       0,0,0,0]

event_map = {
        'w': {'func':work,
              'args':(arr, BY_COLUMN, False)
              },
        'a': {'func':work,
              'args':(arr, BY_ROW, False)
              },
        's': {'func':work,
              'args':(arr, BY_COLUMN, True)
              },
        'd': {'func':work,
              'args':(arr, BY_ROW, True)
              },
        'n': {'func':add_new_elem,
              'args':(arr, 2, True)
              },

    }

##################################################

def getKey():
    q=raw_input()
    return q[0]

out(arr)
k=True
while k:
    k=getKey()
    if k in event_map:
        func=event_map[k]
        arr=func['func'](*func['args'])
        out(arr)
    else: k=False

# print(DIRECTIONS[BY_ROW](1))


