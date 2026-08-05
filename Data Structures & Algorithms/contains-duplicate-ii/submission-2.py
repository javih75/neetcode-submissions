class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        h = set()
        for i, v in enumerate(nums):
            if v in h:
                return True
            h.add(v)
            if len(h) > k:
                h.remove(nums[i-k])
        return False