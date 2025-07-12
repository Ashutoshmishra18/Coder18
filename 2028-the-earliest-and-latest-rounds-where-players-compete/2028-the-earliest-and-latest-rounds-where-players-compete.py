class Solution:
    def earliestAndLatest(self, n, firstPlayer, secondPlayer):
        left = min(firstPlayer, secondPlayer)
        right = max(firstPlayer, secondPlayer)

        if left + right == n + 1:
            return [1, 1]

        if n == 3 or n == 4:
            return [2, 2]

        if left - 1 > n - right:
            temp = n + 1 - left
            left = n + 1 - right
            right = temp

        nextRound = (n + 1) // 2
        minRound = n
        maxRound = 1

        if right * 2 <= n + 1:
            preLeft = left - 1
            midGap = right - left - 1
            for i in range(preLeft + 1):
                for j in range(midGap + 1):
                    res = self.earliestAndLatest(nextRound, i + 1, i + j + 2)
                    minRound = min(minRound, 1 + res[0])
                    maxRound = max(maxRound, 1 + res[1])
        else:
            mirrored = n + 1 - right
            preLeft = left - 1
            midGap = mirrored - left - 1
            innerGap = right - mirrored - 1
            for i in range(preLeft + 1):
                for j in range(midGap + 1):
                    res = self.earliestAndLatest(nextRound, i + 1, i + j + 1 + (innerGap + 1) // 2 + 1)
                    minRound = min(minRound, 1 + res[0])
                    maxRound = max(maxRound, 1 + res[1])

        return [minRound, maxRound]
