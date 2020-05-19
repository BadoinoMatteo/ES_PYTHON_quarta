import threading
import logging
import random

totalebiglietti=100

def cassa1(tID):
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

def cassa2(tID):
    s2.acquire()
    print("cassa 2")
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

    s2.release()

if __name__ == '__main__':
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    t1 = []
    t2=[]

    s1 = threading.Lock()
    s2=threading.Lock()

    for i in range(10):
        t1.append(threading.Thread(target=cassa1, args=(int(i+1), )))
        t2.append(threading.Thread(target=cassa2, args=(int(i + 1),)))
        t1[i].start()
        t2[i].start()



    for i,t in enumerate(t1):
        t.join()

    for i, t in enumerate(t2):
        t.join()
