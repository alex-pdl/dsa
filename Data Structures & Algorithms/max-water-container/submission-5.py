class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # least space
        max_area = 0
        left = 0
        right = len(heights) - 1

        while left < right:
            
            if (right - left) * min(heights[left], heights[right]) > max_area: 
                max_area = (right - left) * min(heights[left], heights[right])

            if heights[left] > heights[right]:
                right -= 1
            elif heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_area