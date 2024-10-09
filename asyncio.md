**Asyncio in Python:**


*What is asyncio?*
asyncio is like having a special helper that lets you play with many toys at once without waiting for one to finish before starting another.

How It Works:
Async: When you say "async," it's like saying, "I want to start playing with this toy, but I’ll come back to it later." You don't have to sit and wait; you can do something else in the meantime.

Await: When you say "await," it’s like saying, "Okay, I’m waiting for my friend to come back with the blocks." You can keep doing other things while you wait.
It allows us to start tasks at A B C D even if the task at A isnt finished yet, 
handle task simutanously, making it more efficient.

>asyncio lets you do many things at once.
>async means starting something and coming back later.
>await means waiting for something to finish but still doing other fun stuff in the meantime.

>>Just like playing with many toys at once, asyncio helps your program be faster and do more things without waiting around!

Let’s say you want to:

Color a picture (this takes some time)
Read a story (this also takes some time)
With asyncio, you can start coloring and then, instead of just waiting for the coloring to finish, you can read the story at the same time!

```py
import asyncio

async def color():
    print("Starting to color...")
    await asyncio.sleep(2)  # Pretend this takes 2 seconds
    print("Finished coloring!")

async def read():
    print("Starting to read...")
    await asyncio.sleep(3)  # Pretend this takes 3 seconds
    print("Finished reading!")

async def main():
    await asyncio.gather(color(), read())

# This starts everything
asyncio.run(main())

```
What Happens Here:


You start coloring.
While you're coloring, you can also read your story.
The await asyncio.sleep() is like taking a break but still getting to enjoy both activities!


Coroutines are special functions in Python that allow you to pause and resume their execution, making them very useful for handling tasks that take time, like waiting for data or performing network operations

What are Coroutines?
Asynchronous Functions: Coroutines are defined using the async def syntax. They can run asynchronously, meaning they can start an operation and then "pause" to let other tasks run.

Pausing with await: Inside a coroutine, you can use the await keyword to pause the function until a certain task is done, like waiting for a response from a server. While waiting, the program can do other work instead of just sitting idle.

Resuming: After the awaited task completes, the coroutine can continue from where it left off

in order for a coroutine to be executed, it eeds to be awaited..

NB!!! when we are creating  a task we are saying it should start as soon as possible and all at once, it shouldnt wait for the other to finish
#create tasks for running coroutines concurrently

```py

async def main():
    task1 = asyncio.create_task(fetch_data(1,2))
    task2 =asyncio.create_task(fetch_data(2,3))
    task= asyncio.create_task(fetch_data(3,1))

```

asynchronous context manager -- asyc **with ** .. They give us access o tg variables
```py
tasks = async with asyncio.TaskGroup () as tg:
for i, sleep_time in enumerate ([2,1,3], start =1):
    task =tg.create_task(fetch_data(i, sleep_time))tasks.append(task)

```

Future-- somethng that will happen in future, getting a value of the future, a promise

**synchronisation **

Lock: we want to lock this
So a lock is used to avoid conflict cause sometimes running stuff at the same time cause cause it
lock = asyncio.Lock()
#will check if something is still using the lock

semaphore: similar to a lock but it allowas multiples code routines at the same time, but you have to say "how many" at a time

event: basic, we can set an event, blocks somethings until it is set, we can set it to true or false
```py
avent.set()
```