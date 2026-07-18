class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i, v in enumerate(nums):
            difference = target - v
            if difference in h:
                return([h[difference], i])
            h[v] = i
