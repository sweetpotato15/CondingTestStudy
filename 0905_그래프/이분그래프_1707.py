'''
sol1) 인접한 node 하나씩 방문하면서 나랑 다른 그룹으로 배정한 뒤 이미 방문된 노드를 
만난다면 나랑 다른지 확인
* 모든 정점에서 확인하고 이상 없으면 YES 임.. 

'''

import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e9))

def dfs(x):
    global group, flag
    visited[x] = 1
    for i in graph[x]:
        if not visited[i]:
            visited[i] = 1
            group[i] = 1-group[x]
            dfs(i)
        elif group[i] == group[x]:
            flag=False

K = int(input())

for _ in range(K):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    group = [-1]*(V+1) # 그룹 정보
    visited = [0]*(V+1) # 방문 여부 
    flag = True

    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, V+1):
        if flag:
            dfs(i)
        else:
            print('NO')
            break
    if flag:
        print('YES')
