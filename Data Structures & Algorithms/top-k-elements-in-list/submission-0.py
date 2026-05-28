import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}
        for n in nums:
            if n in frequencies:
                frequencies[n] += 1
            else:
                frequencies[n] = 1
        
        max_heap = []
        for n,freq in frequencies.items():
            heapq.heappush(max_heap, (-freq, n))

        final = []
        for i in range(k):
            final.append(heapq.heappop(max_heap)[1])

        return final