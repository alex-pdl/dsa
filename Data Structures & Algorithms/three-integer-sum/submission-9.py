class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []

        nums = sorted(nums)

        for i, a in enumerate(nums):
            if a == nums[i-1] and i != 0: continue

            j = i + 1
            k = len(nums) - 1
            
            while j < k:
                sum_of_triple = a + nums[j] + nums[k]

                if sum_of_triple > 0:
                    k -= 1

                elif sum_of_triple < 0:
                    j += 1
                
                else:
                    triple = [a, nums[j], nums[k]] 
                    triplets.append(triple)
                    j += 1
                    while nums[j-1] == nums[j] and j < k:
                        j += 1
        return triplets