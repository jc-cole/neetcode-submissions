class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # total water = (left - right) * min(heights[left], heights[right])
        max = -1
        left = 0
        right = len(heights) - 1
        while left < right:
            area = (right - left) * min(heights[left], heights[right])
            if area > max:
                max = area
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return max