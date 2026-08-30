class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3: return 0
        
        filled_in = height.copy()
        left, right = 0, len(height) - 1
        
        level = 0
        while left < right:
            curr_min = min(filled_in[left], filled_in[right])
            
            level = max(curr_min, level)
            
            if filled_in[left] < filled_in[right]:
                left += 1
            else:
                right -= 1
            
            filled_in[left] = max(filled_in[left], curr_min)
            filled_in[right] = max(filled_in[right], curr_min)

        return sum([filled_in[i] - height[i] for i in range(len(height))])



            