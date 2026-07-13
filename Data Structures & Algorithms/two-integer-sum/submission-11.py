class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i, num in enumerate(nums, start=0):
            difference = target - num
            if difference in h:
                return([h[difference], i])
            elif num not in h:
                h[num] = i