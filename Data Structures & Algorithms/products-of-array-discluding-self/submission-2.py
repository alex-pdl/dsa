class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # With division
        product = 1
        arr = [1] * len(nums)
        no_of_zeros = 0

        for i in nums:
            if i == 0: no_of_zeros += 1
        
        if no_of_zeros > 1:
            return [0] * len(nums)
        
        for i in nums:
            if i == 0: continue

            product *= i
        
        print(product)

        for j in range(len(nums)):
            if nums[j] == 0:
                arr[j] = product
                continue
            
            if no_of_zeros > 0:
                arr[j] *= 0
                continue
            
            arr[j] = product // nums[j]
        
        return arr