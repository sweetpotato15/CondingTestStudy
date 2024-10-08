import sys
input = sys.stdin.readline
INF = int(1e9)
n = int(input())
m = int(input())

graph = [[INF]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)


for k in range(1, n+1): # 거쳐가는 도시 
    for i in range(1, n+1): # 출발 도시
        for j in range(1, n+1): # 도착 도시
            if i == j:
                continue
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF:
            graph[i][j] = 0
    print(*graph[i][1:])