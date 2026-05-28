class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return Solution.mergeSort(nums)

    @staticmethod
    def mergeSort(nums):
        if len(nums) <= 1:
            return nums
        middle = len(nums) // 2
        left = Solution.mergeSort(nums[:middle])
        right = Solution.mergeSort(nums[middle:])
        return Solution.merge(left, right)

    @staticmethod
    def merge(l1, l2):
        i, j = 0, 0
        merged = []
        while i < len(l1) and j < len(l2):
            if l1[i] < l2[j]:
                merged.append(l1[i])
                i += 1
            else:
                merged.append(l2[j])
                j += 1
        merged.extend(l1[i:])
        merged.extend(l2[j:])
        return merged
        