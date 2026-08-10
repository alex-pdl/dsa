class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == k:
            return nums

        frequency = {}

        for i in nums:
            if i not in frequency:
                frequency[i] = 0
            
            frequency[i] += 1

        max_freq = max(frequency.values())

        buckets = [[] for i in range(max_freq)]

        for num in list(frequency.keys()):
            bucket = frequency[num]
            buckets[bucket-1].append(num)

        
        items = []
        for i in range(len(buckets)-1, -1,-1):
            for num in buckets[i]:
                items.append(num)

        return items[:k]