import threading
import time

counter = threading.Lock()

def student(name, priority):
    while True:
        if priority:
            if counter.acquire(blocking=False):
                print(name, "got food")
                time.sleep(1)
                counter.release()
                break
        else:
            print(name, "is waiting for food")
            time.sleep(0.5)

t1 = threading.Thread(target=student, args=("Student 1", True))
t2 = threading.Thread(target=student, args=("Student 2", True))
t3 = threading.Thread(target=student, args=("Student 3", False))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()