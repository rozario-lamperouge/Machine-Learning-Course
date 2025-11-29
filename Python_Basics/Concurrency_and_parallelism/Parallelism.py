# Multiprocessing → runs separate processes with their own Python interpreter and memory.
# Avoids GIL → true parallelism on multiple cores.
# Best for CPU-bound tasks.

from multiprocessing import Process, cpu_count
import time, os

def compute(name, n):
    print(f"Process {name} started (pid={os.getpid()})")
    total = 0
    for i in range(n):
        total += i*i
    print(f"Process {name} finished with result={total}")

start = time.time()
compute("Main", 10000000)
compute("Child", 10000000)
compute("Child", 10000000)
compute("Child", 10000000)
print("Total time:", time.time() - start)

# if __name__ == "__main__":
#     start = time.time()
#     procs = []
#     for i in range(cpu_count()):  # spawn processes equal to number of cores
#         print("i =", i)
#         p = Process(target=compute, args=(f"P{i+1}", 10_000_00))
#         p.start()
#         procs.append(p)
#     for p in procs:
#         p.join()
#     print("Total time:", time.time() - start)
