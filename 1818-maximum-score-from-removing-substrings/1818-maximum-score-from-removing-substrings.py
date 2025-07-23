class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        score = 0
        ch1, ch2 = 'a', 'b'
        count1 = count2 = 0

        if x < y:
            x, y = y, x
            ch1, ch2 = 'b', 'a'

        for ch in s:
            if ch == ch1:
                count1 += 1
            elif ch == ch2:
                if count1 > 0:
                    count1 -= 1
                    score += x
                else:
                    count2 += 1
            else:
                score += min(count1, count2) * y
                count1 = count2 = 0

        if count1 != 0:
            score += min(count1, count2) * y

        return score