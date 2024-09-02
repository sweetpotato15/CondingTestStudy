'''
한 노드에서 시작했을 때 depth가 4이상이면 성공
'''

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(graph, visited, v, count):
    global answer
    if count == 5:
        answer = 1
        return 
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            visited[i] = True
            dfs(graph, visited, i, count+1)
            visited[i] = False

N, M = map(int, input().split())
graph = [[] for _ in range(N)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

answer = 0
for i in range(N):
    visited = [False]*N
    dfs(graph, visited, i, 1)
    if answer:
        print(1)
        exit()
print(0)