class Solution:
    def trap(self, height: list) -> int:
        left_bound, max_left = 0, 0
        right_bound, max_right = len(height) - 1, 0
        volume_count: int = 0
        while left_bound < right_bound:
            max_left = max(max_left, height[left_bound])
            max_right = max(max_right, height[right_bound])
            if height[left_bound] < height[right_bound]:
                if height[left_bound] < max_left:
                    volume_count += max_left - height[left_bound]
                left_bound += 1
            if height[left_bound] >= height[right_bound]:
                if height[right_bound] < max_right:
                    volume_count += max_right - height[right_bound]
                right_bound -= 1
        return volume_count

    def stack_trap(self, height: list) -> int:
        stack: list = [height[0], height[1]]
        volume: int = 0
        for i in range(2, len(height)):
            if height[i] < stack[-1]:
                stack.append(i)
            elif height[i] > stack[-1]:
                while stack and stack[-1] < height[i]:
                    top = stack.pop(-1)
                    if not stack: break
                    volume += (i - top) * (stack[-1] - height[top])
                stack.append(i)
        return volume

s = Solution()
print(s.stack_trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
