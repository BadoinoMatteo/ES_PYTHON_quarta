import threading
import logging
import time


def fn_thread(val):
    s.acquire()
    logging.info("thread %s: inizio", val)
    time.sleep(2)
    logging.info("thread %s: fine", val)
    s.release()

def main():

    format = "%(asctime)s: %(message)a"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M: %S")
    logging.info("padre: creo un thread")

    threads = list()
    for i in range(5):
        logging.info("padre: creo ed avvio thread %d ", i)
        x = threading.Thread(target=fn_thread, args=(i,))
        x.start()

        s = threading.Lock()
        s.acquire()

    for i, t in enumerate(threads):
        logging.info(f"padre: prima dell'attesa del thread {i} ")
        x.join()
        logging.info(f"padre: thread {i} terminato")

    logging.info("padre: fine")

if __name__ == '__main__':
    main()