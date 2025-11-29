# Threading = lightweight units of execution within a process.
# Python’s Global Interpreter Lock (GIL) means only one thread runs Python bytecode at a time.
# Good for I/O-bound tasks, not for CPU-heavy tasks.

import threading
import time

def worker(name, delay):
    print(f"{name} started")
    time.sleep(delay)   # blocking sleep
    print(f"{name} finished after {delay} sec")

threads = []
start = time.time()
for i in range(3):
    t = threading.Thread(target=worker, args=(f"Thread-{i+1}", i+1))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print("Total time:", time.time() - start)
