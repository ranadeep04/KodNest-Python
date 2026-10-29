import threading
import time

pen = threading.Lock()
book = threading.Lock()

def student1():
    pen.acquire()
    print("Student 1 has the pen")

    time.sleep(5)

    print("Student 1 is waiting for the book")
    book.acquire()

    print("Student 1 is writing")
    book.release()
    pen.release()

def student2():
    book.acquire()
    print("Student 2 has the book")

    time.sleep(5)

    print("Student 2 is waiting for the pen")
    pen.acquire()

    print("Student 2 is writing")
    pen.release()
    book.release()

t1 = threading.Thread(target=student1)
t2 = threading.Thread(target=student2)

t1.start()
t2.start()

t1.join()
t2.join()