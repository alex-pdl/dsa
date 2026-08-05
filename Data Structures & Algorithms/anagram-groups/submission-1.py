class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        all_anagrams = []
        while strs:
            i = 0
            j = len(strs) - 1
            anagrams = []
            anagrams.append(strs[i])
            while j != i:
                if sorted(strs[i]) == sorted(strs[j]):
                    anagrams.append(strs[j])
                    strs.pop(j)
                j -= 1
            strs.pop(i)
            all_anagrams.append(anagrams)
        return all_anagrams
