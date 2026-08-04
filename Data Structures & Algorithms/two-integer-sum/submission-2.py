class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,j in enumerate(nums):
            for d,x in enumerate(nums):
                if d <= i:
                    continue
                if j + x == target:
                    return [i,d]