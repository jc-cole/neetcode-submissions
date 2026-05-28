class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)-1):
            prefix *= nums[i]
            ans[i+1] = int(prefix)

        print(ans)
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            ans[i] *= int(postfix)
            postfix *= nums[i]
        return ans

