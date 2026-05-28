class Solution: 
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        for num in nums:
            if num in freqs:
                freqs[num] += 1
            else:
                freqs[num] = 1
        
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, freq in freqs.items():
            buckets[freq].append(num)
        
        most_frequent = []
        for bucket in buckets[::-1]:
            for item in bucket:
                k -= 1
                most_frequent.append(item)
                if k == 0:
                    return most_frequent
        