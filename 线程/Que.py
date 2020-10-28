import threading
from queue import Queue

q = Queue()
threats_list:list = []
def work(data:list, q:Queue):
    q.put([i*i for i in data])
res = []

#创建四个线程并加入线程列表
data = [[i for _ in range(3)] for i in range(1,5)]
for i in range(4):
    t = threading.Thread(target=work, args=(data[i],q))
    t.start()
    threats_list.append(t)

for threat in threats_list:
    threat.join()
for _ in range(4):
    res.append(q.get())

print(res)