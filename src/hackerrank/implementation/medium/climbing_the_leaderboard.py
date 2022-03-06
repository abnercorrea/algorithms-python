def climbingLeaderboard(ranked, player):
    ranks = [0] * len(player)
    n = len(ranked)
    j = 0
    rank = 1
    
    for i in range(len(player) - 1, -1, -1):
        score = player[i]
        
        while (j < n and score < ranked[j]):
            j += 1
            if j == n or ranked[j] != ranked[j - 1]:
                rank += 1   
        
        ranks[i] = rank
        
    return ranks
