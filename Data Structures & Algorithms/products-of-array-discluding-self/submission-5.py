class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Without division
        n = len(nums)
        prev_suff_products = {}
        arr = [1] * n

        left_to_right_product = 1
        right_to_left_product = 1

        for i in range(n):
            arr[i] = left_to_right_product
            left_to_right_product *= nums[i]
        
        for i in range(n-1, -1, -1):
            arr[i] *= right_to_left_product
            right_to_left_product *= nums[i]

        return arr