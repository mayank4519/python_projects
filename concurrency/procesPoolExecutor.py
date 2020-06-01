import time
from concurrent.futures import ProcessPoolExecutor

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

with ProcessPoolExecutor(max_workers=2) as pool:
    pool.submit(do_math)
    pool.submit(do_math)

print(f"Total time taken by 2 process: {time.time() - start}")