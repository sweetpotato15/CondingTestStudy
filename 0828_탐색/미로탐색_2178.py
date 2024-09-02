import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
graph = [[0]*(M+2)] + [[0]+list(map(int, input().strip()))+[0] for _ in range(N)] + [[0]*(M+2)]
visited = [[False]*(M+2) for _ in range(N+2)]

def bfs(x, y):
    if x == N and y == M:
        return
    visited[x][y] = True
    q = deque([(x,y)])

    while q:
        i, j = q.popleft()
        for (di, dj) in ((-1,0),(1,0),(0,-1),(0,1)):
            nx = i + di
            ny = j + dj
            if graph[nx][ny] != 0 and not visited[nx][ny]:
                q.append((nx,ny))
                graph[nx][ny] = graph[i][j] + 1
                visited[nx][ny] = True

bfs(1, 1)
print(graph[N][M])