import asyncio
import time

# Without asyncio
def task(name, delay):
    print(f"{name} started")
    time.sleep(delay)
    print(f"{name} finished after {delay} sec")

def main():
    start = time.time()
    task("Task1", 2)
    task("Task2", 3)
    task("Task3", 1)
    print("Total time:", time.time() - start)

# with asyncio
async def astask(name, delay):
    print(f"{name} started")
    await asyncio.sleep(delay)   # non-blocking sleep
    print(f"{name} finished after {delay} sec")

async def asmain():
    start = time.time()
    await asyncio.gather(
        astask("Task1", 2),
        astask("Task2", 3),
        astask("Task3", 1),
    )
    print("Total time:", time.time() - start)

asyncio.run(asmain())
# main()
