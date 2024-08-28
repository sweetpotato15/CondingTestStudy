import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e8))


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False] * (N+1)
ans = 0

def dfs(graph,v):
    global ans, visited
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            visited[i] = True
            dfs(graph,i)

for i in range(1, N+1):
    if not visited[i]:
        ans += 1
        dfs(graph,i)

print(ans)