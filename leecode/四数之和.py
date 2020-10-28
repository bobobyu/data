import itertools
class Solution:
    def __init__(self):
        self.iter_list: list = []

    def fourSum(self, nums: list, target: int) -> list:
        for i in itertools.combinations(nums, 4):
            if sum(i) == target:
                self.iter_list.append(i)
        return list({tuple(sorted(i)) for i in self.iter_list})

a = Solution()
print(a.fourSum(nums=[1, 0, -1, 0, -2, 2], target=0))
