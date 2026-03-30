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
            print(l,r,s[l:r+1])
            if s[r] in tSet:
                sSet[s[r]] = sSet.get(s[r],0) + 1
                if sSet[s[r]] <= tSet[s[r]]:
                    m += 1
            if m < len(t):
                r += 1
                print("m ", m)
            else:
                print("m ", m)
                while m == len(t):
                    if s[l] in tSet:
                        # print(s[l],sSet[s[l]],tSet[s[l]])
                        sSet[s[l]] -= 1
                        if sSet[s[l]] < tSet[s[l]]:
                            m -= 1
                            print(m)
                            if len(best) > r - l:
                                best = s[l:r+1]
                            print("best so far ", best)
                    l += 1
                r += 1
            print(sSet)
        if len(best) > len(s):
            return ""
        else:
            return best
                
                
                

        