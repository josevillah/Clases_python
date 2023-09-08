import asyncio
import time
import random

async def get_lista(number):
    array = []
    for n in range(number):
        array.append(n)
    return array    


async def lista(num: int):
    for _ in range(num):
        number = await get_lista(num)
        yield number


async def main():
    print('')
    inicio = time.time()
    numbers = [number async for number in lista(3001)]
    print(numbers)
    fin = time.time()
    print('')
    print(fin - inicio)
    

def numberList(number: int):
    array = []
    for n in range(number):
        array.append(n)
    return array

asyncio.run(main()) # 0.05616402626037598




