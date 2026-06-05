class Solution:

    def twoSum(self, nums, target_idx):
        target = nums[target_idx] * -1
        seen = {}
        found_triplets = set()
        for idx in range(len(nums)):
            if idx == target_idx:
                continue
            if target - nums[idx] in seen:
                triplet = []
                triplet.append(nums[idx])
                triplet.append(target - nums[idx])
                triplet.append(nums[target_idx])
                found_triplets.add(tuple(sorted(triplet)))
            else:
                seen[nums[idx]] = idx
        return found_triplets

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets_set = set()
        for idx in range(len(nums)):
            res_triplets = self.twoSum(nums, idx)
            for triplet in res_triplets:
                triplets_set.add(triplet)
        
        return list(triplets_set)
        

        
