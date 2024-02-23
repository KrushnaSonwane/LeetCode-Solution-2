class Solution:
    def countDivisibleSubstrings(self, word: str) -> int:
        A = [[1, 'ab'], [2, 'cde'], [3, 'fgh'], [4, 'ijk'], [5, 'lmn'], [6, 'opq'], [7, 'rst'], [8, 'uvw'], [9, 'xyz']]
        hashT, res = {}, 0
        for size, s in A:
            for ch in s: hashT[ch] = size
        for i in range(len(word)):
            size, sum_ = 0, 0
            for j in range(i, len(word)):
                sum_ += hashT[word[j]]
                size += 1
                res += sum_ % size == 0
        return res