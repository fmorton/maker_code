import asyncio
import random


async def drive(queue):
    print("Consumer task running...")
    while True:
        # Wait for data to arrive in the queue
        data = await queue.get()
        if data is None:  # Signal to stop the consumer
            print("Consumer task stopping.")
            break
        print(f"Processing data: {data}")
        await asyncio.sleep(1)  # Simulate some work


async def producer_task(queue):
    print("Producer task running...")
    for i in range(5):
        value = random.randint(1, 100)
        await queue.put(f"Item {i}, Value {value}")
        print(f"Produced Item {i}")
        await asyncio.sleep(0.5)  # Simulate some work

    # Send a stop signal to the consumer
    await queue.put(None)
    print("Producer task stopping.")


async def main():
    # Create a queue shared by both tasks
    driver_queue = asyncio.Queue()

    # Create and run the producer and consumer tasks
    producer = asyncio.create_task(producer_task(driver_queue))
    consumer = asyncio.create_task(drive(driver_queue))

    # Wait for both tasks to complete
    await asyncio.gather(producer, consumer)


if __name__ == "__main__":
    asyncio.run(main())
