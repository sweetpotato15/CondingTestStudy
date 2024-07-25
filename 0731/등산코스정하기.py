'''
출발지에서 정상까지 가는 길을 최소로 만들면 편도만 구하면 된다. (왕복 고려x)
-> 힙 자료구조 이용

출발지와 도착지를 지정해서 탐색하기 보다는 모든 출발지를 q에 넣고 제일 먼저 도착하는 지점을 return 할 수 있도록 ()
-> 여기서 강도가 같다면 도착지 summit 번호가 제일 작은걸 return 해야함
'''
import heapq
from math import inf

def solution(n, paths, gates, summits):
    graph = [[] for _ in range(n+1)] # (도착지, 비용)
    for i,j,w in paths:
        graph[i].append([j,w])
        graph[j].append([i,w])
    
    # 모든 출발지 넣기
    distance = [inf] * (n+1) # 어떤 출발지에서 i까지의 최대 강도
    q = []
    for gate in gates:
        distance[gate] = 0
        heapq.heappush(q, (0,gate))
    
    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist or node in summits:
            continue
            
        for n_node, value in graph[node]:
            value = max(value, distance[node])
            if distance[n_node] > value:
                distance[n_node] = value
                heapq.heappush(q, (value, n_node))
                
    result = [-1, inf]
    for summit in sorted(summits):
        if distance[summit] < result[1]:
            result[0] = summit
            result[1] = distance[summit]
            
    return result

