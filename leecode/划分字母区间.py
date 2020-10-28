class Solution:
    def partitionLabels(self, S: str) -> list:
        letter_local: dict = {}
        reverse_string = S[::-1]
        length = len(S)
        for i in range(97, 123):
            curr_char = chr(i)
            end_local = reverse_string.find(curr_char)
            if end_local >= 0:
                letter_local[curr_char] = length - end_local - 1
        split_list: list = []
        max_end_local: int = 0
        start_point: int = 0
        end_point: int = 0
        while end_point < length:
            max_end_local = max(max_end_local, letter_local[S[end_point]])
            if end_point == max_end_local:
                split_list.append(end_point - start_point + 1)
                start_point = end_point + 1
                end_point += 1
            else:
                end_point += 1
        return split_list


s = Solution()
print(s.partitionLabels("ababcbacadefegdehijhklij"))
