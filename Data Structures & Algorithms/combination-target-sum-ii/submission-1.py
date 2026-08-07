class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def search(arr, localTarget, banned):
            if len(arr) == 1:
                return [arr] if arr[0] == localTarget and arr[0] not in banned else []
            
            result = []
            withBanned = banned.copy()
            withBanned.add(arr[-1])
            if arr[-1] == localTarget and arr[-1] not in banned:
                result.append([arr[-1]])
            elif arr[-1] <= localTarget and arr[-1] not in banned:
                #consume + not ban
                result.extend([
                    [arr[-1]] + res for res in search(arr[:-1], localTarget - arr[-1], banned)
                ])
            
            #not consume + ban
            result.extend(search(arr[:-1], localTarget, withBanned))
            return result
        
        return search(candidates, target, set())

            
