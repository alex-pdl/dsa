class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        dict_1 = {}
        dict_2 = {}
        
        for i in s:
            if i not in dict_1:
                dict_1[i] = 1
            dict_1[i] += 1
        
        for i in t:
            if i not in dict_2:
                dict_2[i] = 1
            dict_2[i] += 1
        
        if dict_1 == dict_2:
            return True

        return False