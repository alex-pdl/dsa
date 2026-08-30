class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3: return 0
        
        filled_in = height.copy()
        left = 0
        right = len(height) - 1

        while left < len(filled_in)-1:
            #print(left, right)
            if filled_in[left] <= 0 or \
                    filled_in[left+1] >= filled_in[left]:
                left += 1
                right = len(filled_in) - 1
                continue

            while right > left+1:
                level = min(filled_in[right], filled_in[left])
                if filled_in[right-1] < level:
                    filled_in[right-1] = level
                right -= 1

            left += 1
            right = len(filled_in) - 1

        #print(filled_in)
        #print(height)

        return sum([filled_in[i] - height[i] for i in range(len(height))])



            