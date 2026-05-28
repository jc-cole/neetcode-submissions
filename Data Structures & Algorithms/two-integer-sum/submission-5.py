class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indicies = {}
        for idx, num in enumerate(nums):
            if target - num in indicies:
                return [indicies[target - num], idx]
            indicies[num] = idx


