class Solution:
    def kConcatenationMaxSum(self, arr: list, k: int) -> int:
        arrs = arr * 2
        s = [0] * len(arrs)
        s[0] = max(arrs[0], 0)
        for i in range(1,len(arrs)):
            s[i] = max(s[i-1] + arrs[i], 0)
        max_s = max(s)
        if k <= 2:
            return max(s[:len(arr)*k])
        return int((max(sum(arr), 0) * (k-2) + max_s) % (1e9+7))
s = Solution()
print(s.kConcatenationMaxSum([1,2],k=1))


