class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }
        for p in s:
            if p in closeToOpen:
                if not bool(stack) or stack.pop() != closeToOpen[p]:
                    return False
            else:
                stack.append(p)
        return not bool(stack)


                
        