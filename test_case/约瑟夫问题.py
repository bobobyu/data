class member_inf:
    def __init__(self,index:int):
        self.index:int = index
        self.visited:bool = False

class member_list:

    total_count:int = 0 #统计队列中的人数

    def __init__(self):
        self.list_:list = []

    def pop(self,index:int):
        self.list_.pop(index)
        member_list.total_count -= 1

    def push(self,index:int):
        self.list_.append(member_inf(index))
        member_list.total_count += 1

out_index:int = 2 #报数为out_index的出队
total_member:int = 5 #初始化人数

out_x:int = 0 #统计一次报数次数
count_x:int = 0 #标记出队位置

Cmember_list:member_list = member_list()
[Cmember_list.push(i) for i in range(1,total_member+1)] #生成成员列表

while [i.visited for i in Cmember_list.list_].count(False) > 1:
    if out_x == out_index - 1 and not Cmember_list.list_[count_x].visited:
        Cmember_list.list_[count_x].visited = True #若报数次数等于出队标记，设置为以访问
        out_x = 0 #下一个人重新报数
    if Cmember_list.list_[count_x].visited:
        count_x += 1
    else:
        count_x += 1
        out_x += 1
    count_x %= Cmember_list.total_count
    out_x %= out_index

[print(i.index) for i in Cmember_list.list_ if not  i.visited]
