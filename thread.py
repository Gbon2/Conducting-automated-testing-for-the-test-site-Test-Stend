from threading import Thread
from time import sleep

def script(text, pause):
    for i in range(10):
        print(text)
        sleep(pause)

thread1 = Thread(target=script, args=("first", 2))
thread2 = Thread(target=script, args=("second", 3))

thread1.start()
thread2.start()

thread1.join()
thread2.join()