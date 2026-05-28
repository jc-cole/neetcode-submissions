import heapq

class Solution: 
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freqs = {}
        for num in nums:
            if num in freqs:
                freqs[num] += 1
            else:
                freqs[num] = 1

        buckets = [[] for i in range(len(nums) + 1)]

        for value, freq in freqs.items():
            buckets[freq].append(value)

        final = []
        for bucket in buckets[::-1]:
            
            for value in bucket:
                final.append(value)
                k -= 1
                if k == 0:
                    return final

        