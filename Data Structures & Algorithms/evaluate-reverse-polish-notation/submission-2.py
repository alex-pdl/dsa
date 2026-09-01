class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if len(stack) == 0:
                stack.append(i)
                continue
            
            if i in ['+', '*', '-', '/']:
                num_2 = int(stack.pop())
                num_1 = int(stack.pop())
                
                if i == '+': stack.append(num_1 + num_2)
                if i == '-': stack.append(num_1 - num_2)
                if i == '*': stack.append(num_1 * num_2)
                if i == '/': stack.append(num_1 / num_2)
            else:
                stack.append(i)
        
        return int(stack[0])