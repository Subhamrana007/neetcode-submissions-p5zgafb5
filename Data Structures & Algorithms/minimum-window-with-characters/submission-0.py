class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT, countS = {}, {}
        res, resLen = [0, 0], float("inf")
        
        # creating a count map for t

        for ch in t:
            countT[ch] = countT.get(ch, 0) + 1

        # creating have and need
        have, need = 0, len(countT)
        l = 0
        for r in range (len(s)):
            ch = s[r]

            countS[ch] = countS.get(ch, 0) + 1

            if ch in countT and countS[ch] == countT[ch]:
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l) + 1

                countS[s[l]] -= 1

                if s[l] in countT and countS[s[l]] < countT[s[l]]:
                    have -= 1 

                l += 1

        l, r = res

        return s[l: r + 1] if resLen != float("inf") else ""







            # if s[ch] in countT:
            #     countS[ch] = countS.get(ch, 0) + 1
            #     if countT[ch] <= countS[ch]:
            #         have += 1
            #     while have == need:
            #         res = [l, r]
            #         resLen = (r - l) + 1
            #         l += 1



