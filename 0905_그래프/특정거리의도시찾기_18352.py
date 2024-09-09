'''
sol1) 일반 dfs 로 했더니 최단 거리를 확인할 수 없음..
-> 인접 리스트 확인해야함
sol2) dfs 시간초과발생.. ->bfs 수정
'''
import sys
input = sys.stdin.readline
from collections import deque

def bfs(start):
    global distance
    q = deque([start])
    visited[start] = True
    distance[start] = 0

    while q:
        now = q.popleft()
        visited[now] = True
        for i in graph[now]:
            if not visited[i]:
                q.append(i)
                distance[i] = min(distance[i], distance[now]+1)
                visited[i] = True

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
distance = [int(1e6)+1] * (N+1)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    
bfs(X)

if K in distance:
    for i in range(N+1):
        if distance[i] == K:
            print(i)
else:
    print(-1)