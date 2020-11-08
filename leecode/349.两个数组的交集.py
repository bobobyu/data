class Solution:
    def intersection(self, nums1: list, nums2: list) -> list:
        self.dict1: dict = {}
        self.dict2: dict = {}
        minlen = len(min(nums1, nums2, key=len))
        def continue_subset(n, dict_id, nums):
            for i in range(1, n+1):
                interval = [0, i]
                while interval[-1] <= len(nums):
                    dict_id[tuple(nums[interval[0]:interval[-1]])] = 1
                    interval = [i+1 for i in interval]
        continue_subset(minlen, self.dict1, nums1)
        continue_subset(minlen, self.dict2, nums2)
        res = []

        flag = True if len(nums1)>= len(nums2) else False
        for j in self.dict2 if flag else self.dict1:
            if len(j) > len(res) and j in self.dict2 :
                res = j
        return list(res)
s = Solution()
print(s.intersection([1,2,2,1],[2,2]))
