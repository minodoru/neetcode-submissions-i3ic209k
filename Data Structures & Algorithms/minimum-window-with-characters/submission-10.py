class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return "" 
        l, r = 0, 0
        tSet = {}
        for c in t:
            tSet[c] = tSet.get(c,0) + 1
        sSet = {}
        m = 0
        best = s + '.'
        while r < len(s):
            if s[r] in tSet:
                sSet[s[r]] = sSet.get(s[r],0) + 1
                if sSet[s[r]] <= tSet[s[r]]:
                    m += 1
            if m < len(t):
                r += 1
            else:
                while m == len(t):
                    if s[l] in tSet:
                        sSet[s[l]] -= 1
                        if sSet[s[l]] < tSet[s[l]]:
                            m -= 1
                            if len(best) > r - l:
                                best = s[l:r+1]
                    l += 1
                r += 1
        if len(best) > len(s):
            return ""
        else:
            return best
                
                
                

        