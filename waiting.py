import asyncio

async def square (num):
    
    return num*num

async def main():
    x=await square(5)
    print("value of x :",x)

    y= await square(10)
    print("Vale of y :",y)

    z=x+y
    print("Summation of x and y :",z)

asyncio.run(main())