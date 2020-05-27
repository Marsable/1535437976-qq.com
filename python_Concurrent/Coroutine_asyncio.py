import asyncio
@asyncio.coroutine

def func01(): # python3.5以前
    for i in range(10):
        print("python是世界上最好的语言")
        yield from asyncio.sleep(1)
async def func02(): # 3.5以后都可以使用
    for i in range(10):
        print("JAVA是全世界最好的语言")
        await asyncio.sleep(1)
if __name__ == '__main__':
    g1 = func01()
    g2 = func02()
    # 创建事件循环
    loop = asyncio.get_event_loop()
    # 监听事件循环
    loop.run_until_complete(asyncio.gather(g1,g2))
    # 关闭事件循环
    loop.close()