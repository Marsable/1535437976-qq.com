import asyncio


async def computer(x,y):
    print(f"computer:{x}+{y}")
    return x+y

async def print_sum(x,y):
    result = await computer(x,y)
    print(f"{x}+{y}={result}")
if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    loop.run_until_complete(print_sum(1,2))

    loop.close()