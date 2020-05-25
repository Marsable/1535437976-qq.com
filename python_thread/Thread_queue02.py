from queue import PriorityQueue

# 优先级队列
mq = PriorityQueue()

# 存放数据
mq.put((2,"MYS"))
mq.put((1,"DJY"))
mq.put((3,"WHH"))
# get()默认空时，等待新数据
print(mq.get())
print(mq.get())
print(mq.get())
