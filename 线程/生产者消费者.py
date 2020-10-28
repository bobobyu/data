import time
import threading
import random


class ResourcePool:
    def __init__(self, size: int):
        self.source_pool: list = [0 for _ in range(size)]  # 设置缓存区
        self.lock: list = [False for _ in range(size)]  # 设置缓冲区锁定

    def _lock(self, index: int):  # 锁定缓存区
        self.lock[index] = True

    def _unlock(self, index: int):  # 解锁缓存区
        self.lock[index] = False


class Producer:
    def __init__(self, name: str, resource_pool: ResourcePool):  # 初始化一个生产者
        self.name = name
        self.resource_pool: ResourcePool = resource_pool
        self.source_pool = resource_pool.source_pool

    def _product_source(self, lock: list):
        while True:
            for index in range(len(self.source_pool)):
                if not self.source_pool[index] and lock[index] == False:  # 生产者找到一个空闲的缓存区
                    self.resource_pool._lock(index=index)  # 对这个操作位置上锁
                    self.source_pool[index] = random.choice([chr(i) for i in range(65, 91)])  # 从A-Z中随机选取以一个作为生产的资源
                    print(
                        f'Resource pool situation: {self.source_pool}\nCurrent number of threads:：{threading.active_count()}\nProducer ID:{self.name}, find an empty source pool ID {index + 1}.\n')
                    self.resource_pool._unlock(index=index)  # 对这个位置解锁
                if index == len(self.source_pool) - 1:
                    print(
                        f'Resource pool situation: {self.source_pool}\nCurrent number of threads:：{threading.active_count()}\nProducer ID:{self.name}, can not find an empty source pool,waiting......\n')
                time.sleep(2)  # 完成一次操作休眠2s.


class Consumer:
    def __init__(self, name: str, resource_pool: ResourcePool):  # 初始化一个消费者
        self.name = name
        self.resource_pool: ResourcePool = resource_pool
        self.source_pool = resource_pool.source_pool

    def _consume_source(self, lock: list):
        while True:
            for index in range(len(self.source_pool)):
                if self.source_pool[index] and lock[index] == False:
                    self.resource_pool._lock(index=index)  # 对这个操作位置上锁
                    self.source_pool[index] = 0  # 消费资源
                    print(
                        f'Resource pool situation: {self.source_pool}\nCurrent number of threads:：{threading.active_count()}\nConsumer ID:{self.name}, find a valid source pool ID {index + 1}.\n')
                    self.resource_pool._unlock(index=index)  # 对这个位置解锁
                    # 对这个位置解锁
                    if index == len(self.source_pool) - 1:
                        print(
                            f'Resource pool situation: {self.source_pool}\nCurrent number of threads:：{threading.active_count()}\nConsumer ID:{self.name}, can not find a valid source pool,waiting......\n')
                    time.sleep(2)  # 完成一次操作休眠2s.


def producer_consumer(pool_size: int, producer_number: int, consumer_number: int):
    initial_source_pool: ResourcePool = ResourcePool(pool_size)
    initial_producer: list = [Producer(str(i), initial_source_pool) for i in range(1, producer_number + 1)]  # 实例化生产者
    initial_consumer: list = [Consumer(str(i), initial_source_pool) for i in range(1, consumer_number + 1)]  # 实例化消费者

    product_threads = [threading.Thread(target=i._product_source, args=(initial_source_pool.lock,)) for i in
                       initial_producer]  # 实例化生产者线程
    consumer_threads = [threading.Thread(target=i._consume_source, args=(initial_source_pool.lock,)) for i in
                        initial_consumer]  # 实例化消费者线程

    for i in product_threads + consumer_threads:
        i.start()  # 启动线程


producer_consumer(pool_size=4, producer_number=3, consumer_number=2)  # 资源池大小：4，生产者数量：3，消费者数量：2
# producer_consumer(pool_size=2, producer_number=1, consumer_number=1)  # 资源池大小：2，生产者数量：1，消费者数量：1
# producer_consumer(pool_size=10, producer_number=10, consumer_number=10)  # 资源池大小：10，多个生产者，多个消费者
