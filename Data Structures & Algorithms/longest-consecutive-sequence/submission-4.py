class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        num_and_sequence = {}
        
        # Adding each num to dict
        for num in nums:
            num_and_sequence[num] = 0


        seq_num = 1

        for num in nums:
            if num_and_sequence[num] != 0: 
                continue

            if num_and_sequence.get(num - 1) is None and \
                num_and_sequence.get(num + 1) is None:
                continue

            num_and_sequence[num] = seq_num

            dist = 1
            while num_and_sequence.get(num - dist) == 0:
                num_and_sequence[num - dist] = seq_num
                dist += 1

            dist = 1
            while num_and_sequence.get(num + dist) == 0:
                num_and_sequence[num + dist] = seq_num
                dist += 1
            
            seq_num += 1
        
        mode = {}
        for val in num_and_sequence.values():
            if val == 0: continue

            if mode.get(val) is None:
                mode[val] = 0
            
            mode[val] += 1

        if len(mode) == 0:
            return 1
        
        return max(mode.values())
