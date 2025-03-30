import os
import time
import threading

def pinger(website):
    os.system("ping {0}".format(url))


start_time=time.time()
urls =["www.google.com","www.facebook.com","www.n12.co.il"]
threads =[]
for url in urls:
    t=threading.Thread(target=pinger, args=(url,))
    threads.append(t)
    t.start()
for thread in threads:
    thread.join()

output = "ping completed in {} seconds".format(time.time()-start_time)
print(output)