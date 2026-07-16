class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_h = {}
        for char in s:
            if char not in s_h:
                s_h[char] = 1
            else:
                s_h[char] += 1

        t_h = {}
        for char in t:
            if char not in t_h:
                t_h[char] = 1
            else:
                t_h[char] += 1

        if s_h == t_h:
            return True
        else:
            return False