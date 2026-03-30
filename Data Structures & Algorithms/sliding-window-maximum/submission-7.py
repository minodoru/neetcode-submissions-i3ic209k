class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        output = []
        l, r = 1, k
        queue = collections.deque()
        queue.append(nums[0])
        for n in nums[l:r]:
            while n > queue[-1]:
                queue.pop()
                if len(queue) == 0:
                    break
            queue.append(n)
        output.append(queue[0])
        while r < len(nums):
            if nums[l-1] == queue[0]:
                queue.popleft()
            while nums[r] > queue[-1]:
                queue.pop()
                if len(queue) == 0:
                    break
            queue.append(nums[r])
            output.append(queue[0])
            l += 1
            r += 1
        return output