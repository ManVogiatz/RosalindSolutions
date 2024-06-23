n, = input("Insert number of months: ")
k = input("Insert number of rabbit litter pairs: ")

def rabbit_pairs(n, k):
    n = int(n)
    k = int(k)
    
    if n == 1 or n == 2:
        return 1

    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 1

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + k * dp[i - 2]
    
    return dp[n]

def generalized_sequence(n, k, base_cases, relation):
    n = int(n)
    k = int(k)
    
    dp = [0] * (n + 1)
    
    for i, value in enumerate(base_cases):
        dp[i + 1] = value
    
    for i in range(len(base_cases) + 1, n + 1):
        dp[i] = relation(dp, i, k)
    
    return dp[n]

def fibonacci_like_relation(dp, i, k):
    return dp[i - 1] + k * dp[i - 2]

base_cases = [1, 1]  # Corresponding to F(1) and F(2)

result = generalized_sequence(n, k, base_cases, fibonacci_like_relation)
print(result)