class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagram_hash_map = {}

        for i in strs:
            count = [0] * 26
            
            for c in i:
                count[ord(c)-97] += 1
                
            
            if tuple(count) not in anagram_hash_map:
                anagram_hash_map[tuple(count)] = [i]
            else:
                anagram_hash_map[tuple(count)].append(i)

        return list(anagram_hash_map.values())