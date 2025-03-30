import os
import threading
startip=[192,168,1,1]
endip="192.168.1.254"

def NetScan():
    while True:
        result = os.popen("ping {0} -n 1".format(".".join(map(str,startip)))).read()
        startip[3]+=1
        output=result.splitlines()
        for line in output:
            if "TTL" in line:
                print(line)
        if ".".join(map(str, startip)) == endip:
            exit(0)
        else:

            continue

t1=threading.Thread(target=NetScan)
t1.start()