import threading
import time


def myFunc():
    time.sleep(4)
    print("myFunc执行了")


if __name__ == '__main__':
    t = threading.Thread(target=myFunc)
    t.setDaemon(True)
    t.start()
    t.join(1)
    print("it's over")