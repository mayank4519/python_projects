#Atomic operations are very important when you have shared data

from threading import Thread
import time
import random
import queue

counter = 0
job_queue = queue.Queue() #things to print out
counter_queue = queue.Queue() #amount by which to increment cuonter


def increment_manager():
    global counter
    while True:
        increment = counter_queue.get() #get() has the locking mechanism.
        old_counter = counter
        counter = old_counter + increment
        job_queue.put((f'Counter value is {counter}','----'))
        counter_queue.task_done() #this unlocks the queue

Thread(target=increment_manager, daemon=True).start()

def printer_manager():
    while True:
        for line in job_queue.get():
            print(line)
        job_queue.task_done()

Thread(target=printer_manager, daemon=True).start()

def increment_counter():
    counter_queue.put(1)

worker_threads = [Thread(target=increment_counter) for thread in range(10)]

for thread in worker_threads:
    thread.start()

for thread in worker_threads:
    thread.join()

counter_queue.join()
job_queue.join()