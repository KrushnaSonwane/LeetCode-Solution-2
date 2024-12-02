class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        arr = sentence.split()
        for i, word in enumerate(arr):
            if searchWord in word and word.index(searchWord) == 0:
                return i + 1
        return -1