'''
https://www.acmicpc.net/problem/13023
'''
'''
트리로 나타냈을 때 깊이가 5면 성공
각각 노드에서 tree 최대 깊이가 5이상이면 성공

sol1) dfs 로 출발 노드부터 깊이가 5이상인지 확인 -> recursion error, 메모리 초과 
sol2) 백트래킹 - n이 5이면 종료 -> 성공
'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v, visited, n):
    global answer
    if n == 5:
        answer = 1
        return 
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            visited[i] = True
            dfs(i, visited, n+1)
            visited[i] = False

answer = 0
for i in range(N):
    visited = [False] * N
    dfs(i, visited,1)
    if answer == 1:
        print(1)
        exit()
print(0)