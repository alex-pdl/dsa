class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3: return 0
        
        filled_in = height.copy()
        left, right = 0, len(height) - 1
        
        level = 0
        while left < right:
            curr_min = min(filled_in[left], filled_in[right])
            if level < curr_min:
                level = curr_min
            
            if filled_in[left] < filled_in[right]:
                left += 1
            else:
                right -= 1
            
            if filled_in[left] < level: filled_in[left] = level
            if filled_in[right] < level: filled_in[right] = level

        return sum([filled_in[i] - height[i] for i in range(len(height))])



            