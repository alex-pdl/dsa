class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Without division
        n = len(nums)
        arr = [1] * n

        prod = 1

        for i in range(n):
            arr[i] = prod
            prod *= nums[i]
        
        prod = 1
        
        for i in range(n-1, -1, -1):
            arr[i] *= prod
            prod *= nums[i]

        return arr