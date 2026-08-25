class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Without division
        prev_suff_products = {}

        left_to_right_product = 1
        right_to_left_product = 1

        for i in range(len(nums)):
            prev_suff_products[i] = [left_to_right_product]
            left_to_right_product *= nums[i]
        
        for i in range(len(nums)-1, -1, -1):
            prev_suff_products[i].append(right_to_left_product)
            right_to_left_product *= nums[i]

        products = [prod[0] * prod[1] for prod in prev_suff_products.values()]
        
        return products