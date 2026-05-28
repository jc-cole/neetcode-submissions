class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = j = k = 0
        for num in nums:
            if num == 2:
                k += 1
            elif num == 1:
                nums[k], nums[j] = nums[j], nums[k]
                k += 1
                j += 1
            elif num == 0:
                nums[k], nums[j] = nums[j], nums[k]
                nums[j], nums[i] = nums[i], nums[j]
                k += 1
                j += 1
                i += 1



        