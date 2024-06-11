class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        counting = [0] * 1001
        res = []
        for n in arr1:
            counting[n] += 1
        
        for n in arr2:
            while counting[n]:
                res.append(n)
                counting[n] -= 1
        
        for i in range(1001):
            while counting[i]:
                res.append(i)
                counting[i] -= 1
        
        return res