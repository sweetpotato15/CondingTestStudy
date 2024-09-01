'''
dfs - 스택, 재귀 / 깊이 우선 탐색 / LIFO
bfs - 큐 / 너비 우선 탐색 / FIFO
'''
import sys
input = sys.stdin.readline
from collections import deque

def dfs(visited, graph, v):
    visited[v] = True
    print(v,end=" ")
    for i in graph[v]:
        if not visited[i]:
            visited[i] = True
            dfs(visited, graph, i)

def bfs(visited, graph, v):
    q = deque([v])
    visited[v] = True
    while q:
        value = q.popleft()
        print(value, end=" ")
        for i in graph[value]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
graph = [sorted(x) for x in graph]

visited_dfs = [False] * (N+1)
visited_bfs = [False] * (N+1)

dfs(visited_dfs, graph, V)
print()
bfs(visited_bfs, graph, V)