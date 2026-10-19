
import os
import time
import multiprocessing

# Функции имитируют работу отделов корпорации
def energy():
    print("Energy Department: working")
    time.sleep(2)

def security():
    print("Security Department: working")
    time.sleep(3)

def research():
    print("Research Department: working")
    time.sleep(1)

def control():
    print("Control Department: working")
    time.sleep(2)

if __name__ == "__main__":
    # Создаём процессы и назначаем им функции
    p1 = multiprocessing.Process(target=energy)
    p2 = multiprocessing.Process(target=security)
    p3 = multiprocessing.Process(target=research)
    p4 = multiprocessing.Process(target=control)

    # Запускаем процессы
    p1.start()
    p2.start()
    p3.start()
    p4.start()

    print("LCOS Process Manager")
    print("Main process ID:", os.getpid())
    print("Energy ID:", p1.pid)
    print("Security ID:", p2.pid)
    print("Research ID:", p3.pid)
    print("Control ID:", p4.pid)

    p1.join()
    p2.join()
    p3.join()
    p4.join()

    print("All departments finished their work.")
