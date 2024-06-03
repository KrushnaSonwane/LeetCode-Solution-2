class Solution(object):
    def appendCharacters(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        ptr1, ptr2 = 0, 0
        m, n = len(s), len(t)
        maxLen = 0
        while m > ptr1 and n > ptr2:
            if s[ptr1] == t[ptr2]:
                ptr2 += 1
                maxLen += 1
            ptr1 += 1
        return n - maxLen