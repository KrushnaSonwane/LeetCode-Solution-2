class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        NA = len(a)
        NB = len(b)
        INF = inf
        
        @cache
        def go(indexa, indexb):
            if indexa == NA:
                return 0
            if indexb == NB:
                return -INF
            
            best = go(indexa, indexb + 1)
            best = max(best, go(indexa + 1, indexb + 1) + a[indexa] * b[indexb])
            
            return best
        return go(0, 0) 