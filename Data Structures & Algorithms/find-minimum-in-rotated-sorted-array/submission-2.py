class Solution:
    def findMin(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        if nums[-1] >= nums[0] and nums[1] >= nums[0]:
            return nums[0]

        low, high = 0, len(nums) - 1
        mid = (low + high) // 2
        while not (
            nums[(mid - 1) % len(nums)] > nums[mid] and
            nums[(mid + 1) % len(nums)] > nums[mid]
        ):
            mid = (low + high) // 2
            diff_low = abs(nums[mid] - nums[low])
            diff_high = abs(nums[mid] - nums[high])
            if diff_low > diff_high:
                high = mid - 1
            elif diff_high > diff_low:
                low = mid + 1
            else:
                return nums[low]
        
        return nums[mid]


