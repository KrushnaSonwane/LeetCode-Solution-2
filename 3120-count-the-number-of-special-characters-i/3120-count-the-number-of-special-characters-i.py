class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        hashT = set()
        for w in word:
            hashT.add(w)
        res = 0
        taken = set()
        for w in word:
            if w.upper() == w and w.lower() in hashT and w.upper() not in taken:
                taken.add(w)
                res += 1
        return res