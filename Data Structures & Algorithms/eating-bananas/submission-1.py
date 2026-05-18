class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l <= r:
            mid = (l + r) // 2
            t = 0
            for p in piles:
                t += math.ceil(p/mid)
            if t > h:
                l = mid + 1
            else:
                r = mid - 1
                k = mid
        
        return k
