import asyncio
import functools

async def computer(x,y):
    print(f"computer:{x}+{y}")
    await asyncio.sleep(1)
    return x+y

async def print_sum(x,y):
    # 创建task
    task = asyncio.create_task(computer(x,y))
    # asyncio.ensure_future()
    # task绑定回调函数
    task.add_done_callback(functools.partial(end, x, y))
    await asyncio.sleep(1)

def end(n, m, t):
    print(f"{n}+{m}={t.result()}")


if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    loop.run_until_complete(print_sum(1,2))

    loop.close()