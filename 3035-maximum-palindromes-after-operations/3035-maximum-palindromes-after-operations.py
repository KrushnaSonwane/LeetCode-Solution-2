class Solution:
    def maxPalindromesAfterOperations(self, words: List[str]) -> int:
        hashT, A = Counter(), sorted([len(w) for w in words])
        res = 0
        for w in words:
            for ch in w:
                hashT[ch] += 1
        odd, even = 0, 0
        for ch in hashT:
            if hashT[ch] % 2: 
                odd += 1
            even += hashT[ch] // 2
        for size in A:
            if size % 2:
                if not odd:
                    if not even: break
                    odd += 1
                    even -= 1
            if even >= size//2:
                res += 1
                even -= size // 2
        return res