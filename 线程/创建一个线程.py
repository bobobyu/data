import threading


def work():
    print(f'This is a new work:{threading.current_thread()}')

print(f'当前线程数：{threading.active_count()}')
print(f'当前线程信息：{threading.enumerate()}')

#创建一个新线程
add_thread = threading.Thread(target=work)
add_thread.start()
add_thread.join()
print(f'当前线程数：{threading.active_count()}')
print(f'当前线程信息：{threading.enumerate()}')


