class Solution:
    def __init__(self):
        self.purchase_strategy: list = []
        self.cost_list: list = []

    def dp(self):
        for i in range(1, len(self.cost_list)):
            print(self.cost_list)
            if i != self.schedule[self.schedule_index]:
                self.cost_list[i] = self.cost_list[i - 1]
            else:
                self.cost_list[i] = min(
                    self.cost_list[max(0, i - 1)] + costs[0],
                    self.cost_list[max(0, i - 7)] + costs[1],
                    self.cost_list[max(0, i - 30)] + costs[2])
                self.schedule_index += 1



    def mincostTickets(self, days: list, costs: list) -> int:
        self.cost_list = [0 for i in range(days[-1] + 1)]
        self.schedule = days
        self.cuurent_date: int = 1
        self.schedule_index: int = 0
        self.dp()
        return self.cost_list[-1]


days = [1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21, 24, 25, 27, 28, 29, 30, 31, 34, 37, 38, 39,
        41, 43, 44, 45, 47, 48, 49, 54, 57, 60, 62, 63, 66, 69, 70, 72, 74, 76, 78, 80, 81, 82, 83, 84, 85, 88, 89, 91,
        93, 94, 97, 99]
costs = [1, 2, 3]
a = Solution()
print(a.mincostTickets(days, costs))
