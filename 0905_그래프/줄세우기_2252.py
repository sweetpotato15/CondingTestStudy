import sys
input = sys.stdin.readline
from collections import deque

def topology_sort():
    q = deque()
    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        print(now, end = ' ')
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

N, M = map(int, input().split()) # N명, M번 비교
graph = [[] for _ in range(N+1)]
indegree = [0]*(N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

topology_sort()