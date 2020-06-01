import time
from multiprocessing import Process

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

process1 = Process(target=do_math)
process2 = Process(target=ask_user)

process1.start()
process2.start()

process1.join()
process2.join()

print(f"Total time taken by 2 process: {time.time() - start}")