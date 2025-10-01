def climb_stairs(n : int) -> int :
    dp = [0] * (n + 1)
    for i in range(3) :
        dp[i] = i # array initialize
    for i in range(3, n + 1) :
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

print(climb_stairs(int(input())))

# 0 -> x
# 1 -> 1
# 2 -> 11, 2
# 3 -> 111, 21, 12
# 4 -> 1111, 22, 112, 211, 121