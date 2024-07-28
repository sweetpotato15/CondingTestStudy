'''
(출발 -> 레버) + (레버 -> 도착)
bfs + dp
dp[i][j] : 출발지에서 [i][j]까지 가는 최단 거리
bfs 2번 돌려서 dp[레버] + dp[도착지]
'''

from math import inf
from collections import deque

def bfs(start, end, graph):
    dp = [[inf]*(len(graph[0])) for _ in range(len(graph))]
    visited = [[False]*(len(graph[0])) for _ in range(len(graph))]

    q = deque([start])
    visited[start[0]][start[1]] = True
    dp[start[0]][start[1]] = 0
    while q:
        ci,cj = q.popleft()
        visited[ci][cj] = True
        for di, dj in ((-1,0),(1,0),(0,1),(0,-1)):
            ni, nj = ci+di, cj+dj
            if graph[ni][nj] != 'X' and not visited[ni][nj]:
                visited[ni][nj] = True
                dp[ni][nj] = min(dp[ni][nj], dp[ci][cj]+1)
                q.append([ni,nj])

    return dp[end[0]][end[1]]

def solution(maps):
    n,m = len(maps), len(maps[0])

    graph = ['X'*(m+2)]
    for i in range(n):
        graph.append('X' + maps[i] + 'X')
        if 'S' in maps[i]:
            start = [i+1, maps[i].index('S') + 1]
        if 'L' in maps[i]:
            lever = [i+1,  maps[i].index('L') + 1]
        if 'E' in maps[i]:
            end = [i+1,  maps[i].index('E') + 1]
    graph.append('X'*(m+2))

    ans = bfs(start, lever, graph) + bfs(lever, end, graph)
    
    if ans == inf:
        return -1
    return ans


print(solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]))
print(solution(["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"]))