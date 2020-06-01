import time
from threading import Thread

def ask_user():
    start = time.time()
    ask_usr = input("Enter your name")
    print(f"Hello, {ask_usr}")
    print(f"ask_usr {time.time() - start}")

def do_math():
    start = time.time()
    print("Start calculation...")
    [i**2 for i in range(2000000)]
    print(f"Calculataion time {time.time() - start}")

start = time.time()
ask_user()
do_math()
print(f"Single thread total time taken {time.time() - start}")

thread1 = Thread(target=do_math())
thread2 = Thread(target=ask_user())

start = time.time()

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(f"Total time taken by 2 threads: {time.time() - start}")