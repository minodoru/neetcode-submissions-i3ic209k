class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        area = 0
        heights.append(0)
        for i, h in enumerate(heights):
            # print(i, h, stack, area)
            s = i
            while len(stack) and h <= stack[-1][0]:
                get = stack.pop()
                area = max(area, get[0]*(i-get[1]))
                s = get[1]
            stack.append([h,s])
        return area
