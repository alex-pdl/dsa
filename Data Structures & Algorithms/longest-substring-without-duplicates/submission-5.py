class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        
        left = 0
        right = 0
        
        sub_str_chars = set()
        max_sub_str_len = 0

        while right < len(s):
            while s[right] in sub_str_chars:
                sub_str_chars.remove(s[left])
                left += 1
            
            sub_str_chars.add(s[right])
            right += 1

            max_sub_str_len = max(
            max_sub_str_len, len(sub_str_chars))
        
        return max_sub_str_len

