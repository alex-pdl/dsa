class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i, n in enumerate(nums):
            hash_map[n] = i

        for i in range(len(nums)):
            diff = target - nums[i]
            
            if i == hash_map.get(diff):
                continue
            
            if diff in hash_map:
                return [i, hash_map.get(diff)]


