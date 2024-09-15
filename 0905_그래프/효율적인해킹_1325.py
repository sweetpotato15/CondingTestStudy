import sys
input = sys.stdin.readline
from collections import deque

def bfs(x):
    global indegree
    q = deque([x])
    visited[x] = 1

    while q:
        now = q.popleft()
        for i in graph[now]:
            if not visited[i]:
                visited[i] = 1
                q.append(i)
                indegree[i] += 1


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
indegree = [0]*(N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

for i in range(1, N+1):
    visited = [0]*(N+1)
    bfs(i)

max_value = 0
for i in range(1, N+1):
    max_value = max(max_value, indegree[i])

for i in range(1,N+1):
    if indegree[i] == max_value:
        print(i, end=" ")