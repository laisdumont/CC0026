import threading
import time
import random

semaforo = threading.Semaphore(3)

def atendimento(i:str):
    semaforo.acquire()
    print(f'Atendimento nº {i}')
    time.sleep(random.randint(3,10))
    semaforo.release()

if __name__=="__main__":
    clients = []
    for i in range(0,30):
        clients.append(threading.Thread(target=atendimento, args=(i,)))
        clients[i].start()
    for i in clients:
        i.join()