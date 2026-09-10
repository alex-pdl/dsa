class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = left

        char_freq = {}
        max_substr = 0
        
        while right < len(s):
            c = s[right]
            
            if char_freq.get(c) is None:
                char_freq[c] = 0
            
            char_freq[c] += 1
                        
            while (right-left)+1 - max(char_freq.values()) > k:
                char_freq[s[left]] -= 1
                left += 1
            
            max_substr = max(max_substr, right-left+1)
                        
            right += 1

        return max_substr