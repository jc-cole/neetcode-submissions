class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def makeSets(arr):

            if len(arr) == 1:
                return [arr]

            toRemove = arr[-1]

            subsetsRemoved = makeSets(arr[:-1])

            subsetsWith = [subset + [toRemove] for subset in subsetsRemoved] + [[toRemove]]
            return subsetsRemoved + subsetsWith
        
        sets = makeSets(nums)
        sets.append([])
        return sets