class Solution:
    def oddString(self, words: List[str]) -> str:
        hashT = defaultdict(list)
        for j, word in enumerate(words):
            ch = ''
            for i in range(1, len(word)):
                ch += str(ord(word[i]) - ord(word[i-1])) + ' '
                # print(ord(word[i]), ord(word[i-1]))
            # print(ch)
            hashT[ch].append(j)
        for ch in hashT:
            if len(hashT[ch]) == 1:
                return words[hashT[ch][0]]
        # print(hashT)
        return ''