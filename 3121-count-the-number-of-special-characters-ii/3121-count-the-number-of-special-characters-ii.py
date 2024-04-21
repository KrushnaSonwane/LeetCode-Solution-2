class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower = defaultdict(list)
        upper = defaultdict(list)
        for i, ch in enumerate(word):
            if ch == ch.lower():
                lower[ch].append(i)
            else:
                upper[ch].append(i)
        taken = set()
        res = 0
        for ch in word:
            if ch == ch.lower():
                if ch not in taken and len(upper[ch.upper()]) >= 1:
                    # print
                    if lower[ch][-1] < upper[ch.upper()][0]:
                        res += 1
                        taken.add(ch)
        return res