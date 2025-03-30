"""import multiprocessing


def counter(number):

    for i in range(number):

        print(i)
if __name__== '__main__':
    for i in range(5):
        multiprocessing.Process(target=counter,args=(100001,))
        counter(100001)"""

import threading


def counter(l):
    for i in range(10000):
        with l:
            print (i)

lock=threading.Lock()
for i in range(100):
   t= threading.Thread(target=counter, args=(lock,))
   t.start()
