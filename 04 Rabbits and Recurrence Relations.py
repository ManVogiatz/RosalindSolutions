n, k = input("Insert generation and litter rabbit pairs: ").split()
def rabbit_pairs(n, k):
    n = int(n)
    k = int(k)

    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 1

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + k * dp[i - 2]
    
    return dp[n]
result = rabbit_pairs(n, k)
print(result)