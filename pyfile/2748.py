# 2748 피보나치 수 2

# a(n) =  a(n-1) + a(n-2)     n>=2

# bottom-up   memoization 방식

n = int(input())
memo = [0] * (n+1)
def fibo(n):
    memo[0] = 0
    memo[1] = 1

    for i in range(2,n+1):
        memo[i] = memo[i-1] + memo[i-2]

    
    return memo[n]


print(fibo(n))
print(memo)