from threading import Thread
from time import sleep

A = 1

def minha_funcao(): 
    global A
    print("[Thread 1] A antes da alteração: %d" %(A))
    sleep(1)
    A *= -10
    print("[Thread 1] A depois da alteração: %d" %(A))

if __name__ == "__main__": 
    thread = Thread(target = minha_funcao)
    thread.start()
    print("[Thread 0] A antes da alteração: %d" %(A))
    A *= 10
    print("[Thread 0] A depois da alteração: %d" %(A))
    thread.join()
    print("A depois do join: %d" %(A))