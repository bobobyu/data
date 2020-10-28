class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        Test_Times: int = minutesToTest // minutesToDie  # 最多可以尝试的次数
        N_length: int = len(bin(buckets)) - 2  # 将桶数转化为二进制至少需要多少位来表示
        split_length: int = N_length // Test_Times  # 根据尝试的次数将二进制分割为多少段
        last_length: int = split_length + N_length % Test_Times  # 考虑到不能整除的情况，将最后一段添上余数部分

        def calculate_req(group: int):
            if group != 1:
                return calculate_req(group=group - 1) + split_length
            elif group == 1:
                return 2 * last_length - split_length

        return calculate_req(group=Test_Times) + split_length


s = Solution()
print(s.poorPigs(1000, 15, 60))
