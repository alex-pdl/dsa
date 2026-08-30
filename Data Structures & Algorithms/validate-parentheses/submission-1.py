class Solution:
    def isValid(self, s: str) -> bool:
        brack_stack = []
        
        for char in s:
            if char in '([{': 
                brack_stack.append(char)
                continue
            elif char in '}])':
                if len(brack_stack) == 0: return False
                
                if char == '}' and brack_stack[-1] == '{': brack_stack.pop()
                elif char == ']' and brack_stack[-1] == '[': brack_stack.pop()
                elif char == ')' and brack_stack[-1] == '(': brack_stack.pop()
                else: return False


        return not bool(len(brack_stack))