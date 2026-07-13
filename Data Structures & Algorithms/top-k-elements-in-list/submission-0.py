class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = {}
        for num in nums:
            h[num] = h.get(num, 0) + 1

        h_new = dict(sorted(h.items(), key=lambda item: item[1], reverse=True))
        result = []
        for i in range(k):
            result.append(list(h_new)[i])

        return (result)