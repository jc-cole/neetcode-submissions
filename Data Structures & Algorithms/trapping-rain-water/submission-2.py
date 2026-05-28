class Solution:
    def trap(self, height: List[int]) -> int:
        total_trapped = 0
        left_idx = 0
        current_pool = 0
        for i in range(len(height)):
            if height[i] >= height[left_idx]:
                total_trapped += current_pool
                current_pool = 0
                left_idx = i
            else:
                current_pool += height[left_idx] - height[i]
        right_idx = len(height) - 1
        current_pool = 0
        for i in range(len(height) - 1, left_idx - 1, -1):
            if height[i] >= height[right_idx]:
                total_trapped += current_pool
                current_pool = 0
                right_idx = i
            else:
                current_pool += height[right_idx] - height[i]
        return total_trapped

