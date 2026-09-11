class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # BRUTE FORCE

        s1_char_count = {}
        for i in s1:
            if s1_char_count.get(i) is None:
                s1_char_count[i] = 0
            s1_char_count[i] += 1

        for l in range(len(s2)):
            substr_char_count = {}
            
            for r in range(l, len(s2)):
                if substr_char_count.get(s2[r]) is None:    
                    substr_char_count[s2[r]] = 0
                
                substr_char_count[s2[r]] += 1
            
                if substr_char_count == s1_char_count:
                    return True
        
        return False