class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        id_stack = []
        for i, t in enumerate(temperatures):
            while len(id_stack) and t > temperatures[id_stack[-1]]:
                result[id_stack[-1]] = i - id_stack[-1]
                id_stack.pop()
            id_stack.append(i)
        return result