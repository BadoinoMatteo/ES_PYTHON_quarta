import threading
import logging
import time

def fn_thread(val):
    logging.info("thread %s: inizio", val)
    time.sleep(2)
    logging.info("thread %s: fine", val)


if __name__ == '__main__':
    format = "%(asctime)s: %(message)a"
    logging.basicConfig(format = format, level= logging.INFO, datefmt="%H:%M: %S")
    logging.info("padre: creo un thread")

    x= threading.Thread(target= fn_thread, args=(1, ))

    logging.info("padre: avvio thread creato")
    x.start()

    logging.info("padre: aspetto la terminazione del thread creato")
    x.join()

    logging.info("padre: fine")