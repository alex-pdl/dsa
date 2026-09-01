class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if not bool(stack):
                stack.append(i)
            elif i in ['+', '*', '-', '/']:
                num_2 = int(stack.pop())
                num_1 = int(stack.pop())
                
                if i == '+': stack.append(num_1 + num_2)
                elif i == '-': stack.append(num_1 - num_2)
                elif i == '*': stack.append(num_1 * num_2)
                elif i == '/': stack.append(num_1 / num_2)
            else:
                stack.append(i)
        
        return int(stack[0])