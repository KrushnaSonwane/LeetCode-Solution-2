class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        i = 0
        for ch in str1:
            if i < len(str2):
                if ch == str2[i]:
                    i += 1
                else:
                    if ch == 'z':
                        if str2[i] == 'a':
                            i += 1
                    else:
                        if str2[i] == chr(ord(ch) + 1):
                            i += 1
        return i == len(str2)