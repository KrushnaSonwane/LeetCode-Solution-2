class Solution:
    def isValid(self, s: str) -> bool:
        vowels = set('aeiouAEIOU')
        has_vowel = False
        has_consonant = False

        for char in s:
            if char in '#$@': return False
            if char.isalpha():
                if char in vowels:
                    has_vowel = True
                else:
                    has_consonant = True

        return len(s) >= 3 and has_vowel and has_consonant
                