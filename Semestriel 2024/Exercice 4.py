def computeNbrOfDifferentSequences(N, C, H):
    dp = {0: 1}

    for i in range(N):
        next_dp = {}
        for s in dp:
            for m in range(1, C + 1):
                next_dp[s + m] = next_dp.get(s + m, 0) + dp[s]
        dp = next_dp
    print(dp)
    return dp.get(H, 0)


print(computeNbrOfDifferentSequences(2,6,7))