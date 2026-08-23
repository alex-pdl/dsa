class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "nothing"
        final_str = ""
        for j in range(len(strs)): # O(m)
            temp_str = ""
            for i in range(len(strs[j])):
                temp_str += str(ord(strs[j][i]))
                if i >= len(strs[j])-1:
                    continue
                temp_str += "_"
            final_str += temp_str
            if j >= len(strs) -1:
                continue
            final_str += "#"
        return final_str

    
    
    def decode(self, s: str) -> List[str]:
        if s == "nothing":
            return []
        ord_words_with_spaces = s.split("#")
        decoded_msg = []
        for i in ord_words_with_spaces:
            encoded_word = i.split('_')
            decoded_word = ""
            for j in encoded_word:
                try:
                    decoded_word += chr(int(j))
                except Exception as e:
                    print(e)
            decoded_msg.append(decoded_word)
        return decoded_msg
