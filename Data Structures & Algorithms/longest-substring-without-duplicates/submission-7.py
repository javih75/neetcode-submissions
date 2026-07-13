class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 1
        count = 1
        maxCount = 1
        seen = set()
        if not s:
            return 0
        seen.add(s[l]) 
        while r < len(s):
            if s[r] in seen:
                maxCount = max(maxCount, count)
                count = 1
                l += 1
                r = l + 1
                seen = set()
                if not s:
                    return 0
                seen.add(s[l]) 
            else:
                count += 1
                seen.add(s[r])
                r += 1
                
        maxCount = max(maxCount, count)
        return maxCount


