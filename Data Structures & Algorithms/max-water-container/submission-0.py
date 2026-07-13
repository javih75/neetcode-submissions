class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        area1 = 0
        while left <= right:
            width = right - left
            minHeight = min(heights[left], heights[right])
            area2 = width * minHeight
            area1 = max(area1, area2)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return area1