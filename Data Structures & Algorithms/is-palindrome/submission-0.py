class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [char for char in s if char.isalnum()]
        s = "".join(s)
        text = s[::-1]

        if text.lower() == s.lower():
            return True
        else:
            return False