class Solution:
    def isPalindrome(self, s: str) -> bool:
        start_ptr = 0
        end_ptr = -1
        
        while True:
            print(s[start_ptr],start_ptr, s[end_ptr], end_ptr+len(s))

            if start_ptr == end_ptr + len(s):
                return True

            if not s[start_ptr].isalnum():
                start_ptr += 1
                continue
            
            if not s[end_ptr].isalnum():
                end_ptr -= 1
                continue

            if s[start_ptr].lower() != s[end_ptr].lower():
                return False

            if start_ptr + 1 == end_ptr + len(s):
                return True
            start_ptr += 1
            end_ptr -= 1

