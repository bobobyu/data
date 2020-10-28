class Solution:
    def __init__(self):
        self.middle_list: list = []
        self.sliding_window: list = []

    def middle_number(self, list_: list):
        length = len(list_)
        middle_index = length // 2
        list_copy = sorted(list_)
        return list_copy[middle_index] if length % 2 else (list_copy[middle_index - 1] + list_copy[middle_index]) / 2

    def medianSlidingWindowdp(self, nums: list, k: int) -> None:
        if k <= len(nums):
            if not self.sliding_window:
                self.sliding_window = nums[:k]
                self.middle_list.append(self.middle_number(self.sliding_window))
                self.medianSlidingWindowdp(nums=nums, k=k + 1)
            else:
                self.sliding_window.pop(0)
                self.sliding_window.append(nums[k - 1])
                self.middle_list.append(self.middle_number(self.sliding_window))
                self.medianSlidingWindowdp(nums=nums, k=k + 1)

    def medianSlidingWindow(self, nums: list, k: int) -> list:
        if nums:
            self.medianSlidingWindowdp(nums=nums, k=k)
            return self.middle_list
        else:
            return []


class Solution_:
    def __init__(self):
        self.middle_list: list = []
    def medianSlidingWindow(self, nums: list, k: int) -> list:
        if nums:
            sliding_window: list = []
            middle_index: list = [k // 2, k//2] if k % 2 else [k // 2, k // 2 - 1]
            while len(nums) >= k:
                if not sliding_window:
                    sliding_window = nums[:k]
                    sliding_window_copy = sorted(sliding_window)
                    self.middle_list.append(sum([sliding_window_copy[i] for i in middle_index]) / 2)
                    nums.pop(0)
                    continue
                sliding_window.pop(0)
                sliding_window.append(nums[k - 1])
                sliding_window_copy = sorted(sliding_window)
                self.middle_list.append(sum([sliding_window_copy[i] for i in middle_index]) / 2)
                nums.pop(0)
            return self.middle_list
        return []


s = Solution_()
a = [1, 3, -1, -3, 5, 3, 6, 7]
print(s.medianSlidingWindow(nums=a, k=3))
