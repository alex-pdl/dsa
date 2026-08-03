class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_2 = {}
        
        for i in nums:
            if i in nums_2:
                return True
            nums_2[i] = 1

        return False
