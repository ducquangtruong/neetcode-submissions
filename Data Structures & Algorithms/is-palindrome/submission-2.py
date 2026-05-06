class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = "".join(filter(lambda x: x.isalnum(), [chr.lower() for chr in s]))
        
        return new_s == new_s[::-1]