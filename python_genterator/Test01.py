import time
import sys
#列表:耗时
# list1 = []
# # 占用内存
# for i in range(2, 10000, 2):
#     list1.append(i)
# print(list1)
# # 列表推导式
# list1 = [x for x in range(2, 100000000, 2)]
# costTime = time.perf_counter()
# print("创建列表推导式耗时：{}".format(costTime))
#
# print("创建列表推导式内存开销：{}".format(sys.getsizeof(list1)))
# print(list1)
# list2 = [x for x in range(1,10) if x%2 == 0]
# print(list2)
# list3 = [a+b for a in "123" for b in "xyz"]
# print(list3)

# 生成器genterator

g1 = (x for x in range(2, 100000000, 2))
costTime = time.perf_counter()
print("创建生成器耗时：{}".format(costTime))
print("创建生成器内存开销：{}".format(sys.getsizeof(g1)))

# print(next(g1))
# for i in g1:
#     print(i)
