import threading
import logging
import random


def cassa():
    totalebiglietti=100
    numeroBiglietti=[0,1,2,3,4,5,6,7,8,9,10]
    biglietti=(int)(1+ random.choice(numeroBiglietti))
    print(totalebiglietti)
    if totalebiglietti==0:     #biglietti esauriti
        print("biglietti esauriti")
    elif totalebiglietti>0 and biglietti<=totalebiglietti:
         print(f"biglietti acquistati {biglietti}" )
         totalebiglietti=totalebiglietti-biglietti
    elif 0 < totalebiglietti < biglietti:
         print("biglietti acquistati = " + totalebiglietti)
         totalebiglietti=0

    s.release()

if __name__ == '__main__':
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    t=[]

    for _ in range(1,10):
        t.append(threading.Thread(format=cassa()))

    s = threading.Lock()
    s.acquire()
    
    print("inizio")
    for i in range(0, 9):
        t[i].start()


    for i in range(0,9):
        t[i].join()
