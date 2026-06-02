class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for ptr in nums:
            if nums[abs(ptr)] < 0:
                for num in nums:
                    num = abs(num)
                    print(nums)
                return abs(ptr)
            else:
                nums[abs(ptr)] = -nums[abs(ptr)]
        