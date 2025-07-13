class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()

        sum=0
        a=b=0
        while a<len(players) and b<len(trainers):
            if players[a]<=trainers[b]:
                sum+=1
                a+=1
                b+=1
            else:
                b+=1
        return sum    