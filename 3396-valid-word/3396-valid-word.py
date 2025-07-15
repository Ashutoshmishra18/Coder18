class Solution:
    def isValid(self, word: str) -> bool:
        if len(word)<3:
            return False
        if not all(c.isalnum() for c in word):
            return False
        vowels=set("aeiouAEIOU")
        has_vowels=any(c in vowels for c in word)
        has_consonant=any(c.isalpha() and c not in vowels  for c in word)
        return has_vowels and has_consonant
        