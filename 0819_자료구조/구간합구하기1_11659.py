import sys
input = sys.stdin.readline

N, M = map(int, input().split())
array = [0] + list(map(int, input().split()))

dp = [0] * (N+1) # dp[i] : array의 i번째 수까지의 합

for i in range(1,N+1):
    dp[i] = dp[i-1] + array[i]

for _ in range(M):
    i, j = map(int, input().split()) # i번째 수 ~ j번째 수까지의 합
    print(dp[j] - dp[i-1])
