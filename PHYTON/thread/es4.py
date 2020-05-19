import threading
import logging
import random

totalebiglietti=100

def cassa(tID):
    s1.acquire()
    print("cassa 1")
    numeroBiglietti=[0,1,2,3,4,5,6,7,8,9,10]
    biglietti=(int)(random.choice(numeroBiglietti))
    global totalebiglietti
    print(totalebiglietti)
    if totalebiglietti==0:     #biglietti esauriti
        print("biglietti esauriti")
    elif totalebiglietti>0 and biglietti<=totalebiglietti:
         print(f"biglietti acquistati {biglietti}" )
         totalebiglietti=totalebiglietti-biglietti
    elif 0 < totalebiglietti < biglietti:
         print(f"biglietti acquistati {totalebiglietti}")
         totalebiglietti=0

    s1.release()


if __name__ == '__main__':
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    t = []

    s1 = threading.Lock()

    for i in range(10):
        t.append(threading.Thread(target=cassa, args=(int(i+1), )))
        t[i].start()



    for i,t in enumerate(t):
        t.join()
