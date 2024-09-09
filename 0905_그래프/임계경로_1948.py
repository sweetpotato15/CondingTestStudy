'''
출발지에서 도착지까지 가능한 모든 경로 탐색하면서 (최단경로가 아님)
최대 시간과 그때의 지나가는 노드 저장해야함
sol1) 일반 dfs - 3퍼 시간초과
sol2) 그래프 역계산 - 순방향으로 위상정렬 실행 후 역방향으로 위상정렬하면서 1분도 쉬면 안되는 것 체크
'''

import sys
input = sys.stdin.readline
from collections import deque

n = int(input()) # 도시 개수
m = int(input()) # 도로 개수
graph = [[] for _ in range(n+1)]
r_graph = [[] for _ in range(n+1)]
indegree = [0]*(n+1)

for _ in range(m):
    s, e, t = map(int, input().split())
    graph[s].append((t,e)) # (시간, 도착점)
    r_graph[e].append((t,s))
    indegree[e] += 1

start, end = map(int, input().split())

q = deque([start])
result = [0]*(n+1)

while q:
    now = q.popleft()
    for next_cost, next_node in graph[now]:
        indegree[next_node] -= 1
        result[next_node] = max(result[next_node], result[now]+next_cost)
        if indegree[next_node] == 0:
            q.append(next_node)

max_count = 0
visited = [False]*(n+1)
q = deque([end])
visited[end] = True

while q:
    now = q.popleft()
    # start~next_node (순방향) 비용 + now~next_node (역방향) 비용 == start~now (순방향) 비용 (최대값)
    for next_cost, next_node in r_graph[now]:
        if result[next_node]+next_cost == result[now]:
            max_count += 1
            if not visited[next_node]:
                visited[next_node] = True
                q.append(next_node)

print(result[end])
print(max_count)