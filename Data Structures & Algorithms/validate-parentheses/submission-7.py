class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if s[0] in [")","]","}"]:
            return False
        for p in s:
            if p == ")":
                print(")", len(stack))
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


                
        