'''
dfs + dp
dp - [i][j]에서부터 이동할 수 있는 칸 수

'''

import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e9))

def dfs(x,y):
    if dp[x][y] == -1:
        dp[x][y] = 1
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni = x+di
            nj = y+dj
            if forest[ni][nj] > forest[x][y]:
                dp[x][y] = max(dp[x][y],dfs(ni,nj) + 1)
    return dp[x][y]


n = int(input())
forest = [[0]*(n+2)] + [[0]+list(map(int, input().split()))+[0] for _ in range(n)] + [[0]*(n+2)]
dp = [[-1]*(n+2) for _ in range(n+2)]

maximum=0
for i in range(1,n+1):
    for j in range(1, n+1):
        maximum = max(maximum, dfs(i,j))
print(maximum)
