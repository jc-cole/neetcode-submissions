class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
        
        m = len(nums1)
        n = len(nums2)
        half = (m + n + 1) // 2

        left, right = 0, m

        while left <= right:
            i = (left + right) // 2
            j = half - i

            leftMax1 = nums1[i - 1] if i > 0 else float("-inf")
            rightMin1 = nums1[i] if i < m else float("inf")

            leftMax2 = nums2[j - 1] if j > 0 else float("-inf")
            rightMin2 = nums2[j] if j < n else float("inf")

            if leftMax1 <= rightMin2 and leftMax2 <= rightMin1:
                if (m + n) % 2 == 1:
                    return max(leftMax1, leftMax2)
                
                leftMax = max(leftMax1, leftMax2)
                rightMin = min(rightMin1, rightMin2)

                return (leftMax + rightMin) / 2
            
            if leftMax1 > rightMin2:
                right = i - 1
            else:
                left = i + 1



