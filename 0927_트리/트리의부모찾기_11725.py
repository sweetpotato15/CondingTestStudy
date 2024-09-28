import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e9))

def dfs(v):
    global answer, visited
    visited[v] = True
    for i in graph[v]:
        if not visited[i] and not answer[i]:
            answer[i] = v
            visited[i] = True
            dfs(i)

N = int(input())
graph = [[] for _ in range(N+1)]
visited = [False]*(N+1)
answer = [0]*(N+1)

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1)
print(*answer[2:], sep='\n')