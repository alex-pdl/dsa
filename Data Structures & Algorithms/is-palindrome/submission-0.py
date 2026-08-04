class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) <= 1:
            return True
        
        if not s[-1].isalnum():
            return self.isPalindrome(s[:-1])
        
        if not s[0].isalnum():
            return self.isPalindrome(s[1:])
        
        if s[0].lower() != s[-1].lower():
            return False
        
        return self.isPalindrome(s[1:-1])