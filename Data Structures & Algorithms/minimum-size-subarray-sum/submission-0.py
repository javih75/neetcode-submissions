class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        total = 0
        ret = float('inf')

        for r in range(len(nums)):
            total += nums[r]

            while total >= target:
                ret = min(ret, r-l+1)

                total -= nums[l]
                l+=1

        if ret == float('inf'):
            return 0
        else:
            return ret
