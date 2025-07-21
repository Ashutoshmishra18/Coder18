class Solution:
    def makeFancyString(self, s: str) -> str:
        res = s[0]
        last = s[0]
        c = 1

        for i in range(1, len(s)):
            if s[i] != last:
                last = s[i]
                c = 0

            c += 1
            if c > 2:
                continue

            res += s[i]

        return res
