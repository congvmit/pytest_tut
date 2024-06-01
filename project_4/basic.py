import asyncio


async def add(a, b):
    print(f"Adding {a} + {b}")
    await asyncio.sleep(1)
    return a + b


async def sub(a, b):
    print(f"Subtracting {a} - {b}")
    await asyncio.sleep(1)
    return a - b


async def main():
    res_add, res_b = await asyncio.gather(add(1, 2), sub(3, 4))
    print(f"Result of add: {res_add} and sub: {res_b}")


if __name__ == "__main__":
    asyncio.run(main())
