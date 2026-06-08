class Solution:
    def binSearch(self, nums, low, high, target):

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
        
        return -1

    def search(self, nums: List[int], target: int) -> int:

        if len(nums) == 1:
            return self.binSearch(nums, 0, 0, target)
        
        if len(nums) == 2:
            left = self.binSearch(nums, 0, 0, target)
            right = self.binSearch(nums, 1, 1, target)
            return max(left, right)
        
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if nums[low] > nums[mid]:
                high = mid - 1
            elif nums[mid] > nums[high]:
                low = mid + 1
            else:
                break
        
        pivot = min(
            [low - 1, low, low + 1],
            key = lambda i : nums[i % len(nums)]
        )

        left = self.binSearch(nums, 0, pivot - 1, target)
        right = self.binSearch(nums, pivot, len(nums) - 1, target)
        return max(left, right)
