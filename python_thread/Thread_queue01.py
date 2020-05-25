from queue import LifoQueue

# 队列后进先出LIFO
mq = LifoQueue()

# 存放数据
mq.put(1)
mq.put(2)
mq.put(3)
# get()默认空时，等待新数据
print(mq.get())
print(mq.get())
print(mq.get())
print(mq.get(block=False)) # block默认为True等待，false为不等待相当于get_nowait()
# get_nowait() 队列为空时，不等待
# print(mq.get_nowait())
