class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3: return 0
        
        left, right = 0, len(height) - 1
        
        level = 0

        water_trapped = 0
        while left < right:
            curr_min = min(height[left], height[right])
            
            level = max(curr_min, level)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            
            water_trapped += max(height[left], level) - height[left]
            water_trapped += max(height[right], level) - height[right]

        return water_trapped



            