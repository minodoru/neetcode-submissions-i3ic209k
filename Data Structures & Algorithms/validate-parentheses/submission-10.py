class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for p in s:
            if p == ")":
                if not bool(len(stack)) or stack.pop() != "(":
                    return False
            elif p == "]":
                if not bool(len(stack)) or stack.pop() != "[":
                    return False
            elif p == "}":
                if not bool(len(stack)) or stack.pop() != "{":
                    return False
            else:
                stack.append(p)
        return not bool(len(stack))


                
        