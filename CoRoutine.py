# import time
# def a():
#     value = b()
#     print(value)

# def b():
#     time.sleep(5)
#     return 5

# a()
# -----------------------------------------------------------------

# import asyncio


# async def main():
#     print("Started")
# # To execute a co routine we need an event loop.asyncio run automatically create this async event loop for us
# asyncio.run(main())


# ---------------------------------------------------------------------

import asyncio
# Create and access a newe asyncio event loop
loop = asyncio.new_event_loop()
# define a task

task1 = asyncio.sleep(2)
# execute the task
loop.run_until_complete(task1)
print("done")