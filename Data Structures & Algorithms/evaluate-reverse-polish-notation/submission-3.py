class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            print(stack)
            if t == '+':
                op = stack.pop() + stack.pop()
                stack.append(op)
            elif t == '-':
                op = - stack.pop() + stack.pop()
                stack.append(op)
            elif t == '*':
                op = stack.pop() * stack.pop()
                stack.append(int(op))
            elif t == '/':
                last = stack.pop()
                op = stack.pop() / last
                stack.append(int(op))
            else:
                stack.append(int(t))
            
        return stack[-1]