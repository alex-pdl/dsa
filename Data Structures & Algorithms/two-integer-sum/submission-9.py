class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        
        for idx, val in enumerate(nums):
            diff = target - val
            
            if diff in hash_map:
                return [hash_map.get(diff), idx]

            hash_map[val] = idx

