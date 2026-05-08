class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)//2
        while r >= l and r < len(nums):
            print(l,r)
            if nums[l] == target:
                return l
            elif nums[r] == target:
                return r
            elif nums[l] > target:
                return -1
            elif nums[r] < target:
                spread = r - l
                l = r + 1
                r = l + spread // 2
            else:
                spread = r - l
                r = l + spread // 2
        return -1
