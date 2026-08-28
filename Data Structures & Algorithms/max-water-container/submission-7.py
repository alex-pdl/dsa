class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(heights) - 1

        while left < right:
            area = (right - left) * min(heights[left], heights[right])
            left_ptr = heights[left]
            right_ptr = heights[right]
            
            if area > max_area: max_area = area

            if left_ptr > right_ptr:
                right -= 1
            elif left_ptr == right_ptr:
                right -= 1
            else:
                left += 1
                

        return max_area