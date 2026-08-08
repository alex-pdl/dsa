class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == k:
            return nums

        frequency = {}

        for i in nums:
            if i not in frequency:
                frequency[i] = 0
            
            frequency[i] += 1

        sorted_by_freq = {k: v for k, v in sorted(frequency.items(), key=lambda item: item[1])}
        
        return list(sorted_by_freq.keys())[-k:]