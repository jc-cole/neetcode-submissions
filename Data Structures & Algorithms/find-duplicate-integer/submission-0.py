class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for ptr in nums:
            if nums[abs(ptr)] < 0:
                return abs(ptr)
            else:
                nums[abs(ptr)] = -nums[abs(ptr)]