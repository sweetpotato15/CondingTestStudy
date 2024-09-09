import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
graph = [[] for _ in range(N+1)]
indegree = [0]*(N+1)
cost = [0]*(N+1)
ans = [0]*(N+1)

for i in range(1,N+1):
    lst = list(map(int, input().split()))
    cost[i] = lst[0]
    for j in lst[1:-1]:
        graph[j].append(i)
        indegree[i] += 1

q = deque()
for i in range(1, N+1):
    if indegree[i] == 0:
        q.append(i)
    ans[i] = cost[i] # i번째 건물 짓는 비용 (모든 건물 자기 비용으로 초기화)

while q:
    now = q.popleft()
    for i in graph[now]: # i: now 짓고 지어야 하는 건물
        indegree[i] -= 1
        ans[i] = max(ans[i], cost[i]+ans[now])
        if indegree[i] == 0:
            q.append(i)

print(*ans[1:], sep='\n')