class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        last = nums.pop()
        permsNoLast = self.permute(nums)
        result = []
        for perm in permsNoLast:
            perm.append(last)
            result.append(perm.copy())
            for i in range(len(perm) - 1, 0, -1):
                perm[i-1], perm[i] = perm[i], perm[i-1]
                result.append(perm.copy())
        return result