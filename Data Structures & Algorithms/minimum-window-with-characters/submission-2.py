class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ""

        countT = {}
        window = {}

        for char in t:
            if char in countT:
                countT[char] += 1
            else:
                countT[char] = 1

        have = 0
        need = len(countT)
        res = [-1, -1]
        resLen = float("infinity")
        left = 0

        for right in range(len(s)):
            char = s[right]

            if char in window:
                window[char] += 1
            else:
                window[char] = 1

            if char in countT and window[char] == countT[char]:
                have += 1

            while have == need:
                if (right - left + 1) < resLen:
                    res = [left, right]
                    resLen = right - left + 1

                window[s[left]] -= 1
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -= 1

                left += 1

        l, r = res
        if resLen != float("infinity"):
            return s[l:r + 1]
        return ""




