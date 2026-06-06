import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        best_k = -1
        while low <= high:
            print(f"low: {low}")
            print(f"high: {high}")
            print(f"best_k: {best_k}")
            mid_k = (low + high) // 2
            hrs_taken = sum(math.ceil(pile_size / mid_k) for pile_size in piles)
            print(f"hrs_taken: {hrs_taken}")
            if hrs_taken > h:
                low = mid_k + 1
            elif hrs_taken <= h:
                best_k = mid_k
                high = mid_k - 1
                
        return best_k
 