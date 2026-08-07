class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        # print(nums)
        # print(target)

        if len(nums) == 0:
            return []

        if len(nums) == 1:
            return [[nums[0] for i in range(target // nums[0])]] if target % nums[0] == 0 else []

        last = nums[-1]
        result = []
        if last == target:
            result.append([last])
        elif last <= target:
            result.extend([[last] + arr for arr in self.combinationSum(nums, target - last)])
        result.extend(self.combinationSum(nums[:-1], target))

        return result


        